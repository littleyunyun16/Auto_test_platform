from django.shortcuts import render
from django.utils.decorators import method_decorator  # method_decorator 是将函数装饰器转换成方法装饰器。


@method_decorator(login_required, name='dispatch')
class InterfaceIndex(ListView):
    model = Interface
    template_name = 'base/interface/index.html'
    context_object_name = 'object_list'
    paginate_by = 10

    def dispatch(self, *args, **kwargs):
        return super(InterfaceIndex, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        interface_list = Interface.objects.all().order_by('-if_id')
        return interface_list

    def get_context_data(self, **kwargs):
        self.page = self.request.GET.dict().get('page', '1')
        context = super().get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        data = pagination_data(paginator, page, is_paginated)
        context.update(data)
        user_id = self.request.session.get('user_id', '')
        model_list = limits_of_authority(user_id)
        context.update({"model_list": model_list, "page": self.page})
        return context

    def interface_copy(request):
        """
        复制interface
        :param request:
        :return:
        """
        user_id = request.session.get('user_id', '')
        if not get_user(user_id):
            request.session['login_from'] = '/base/case/'
            return render(request, 'user/login_action.html')
        else:
            if request.method == 'GET':
                if_id = request.GET.get('if_id', '')
                interface_ = Interface.objects.get(if_id=if_id)
                if_name = interface_.if_name + 'copy'
                url = interface_.url
                method = interface_.method
                data_type = interface_.data_type
                is_sign = interface_.is_sign
                is_header = interface_.is_header
                mock = interface_.set_mock
                skip = interface_.skip
                description = interface_.description
                request_header_param = interface_.request_header_param
                request_body_param = interface_.request_body_param
                response_header_param = interface_.response_header_param
                response_body_param = interface_.response_body_param
                project = interface_.project
                username = request.session.get('user', '')
                interface = Interface(if_name=if_name, url=url, project=project, method=method, data_type=data_type,
                                      is_sign=is_sign, description=description,
                                      request_header_param=request_header_param,
                                      request_body_param=request_body_param,
                                      response_header_param=response_header_param,
                                      response_body_param=response_body_param, is_header=is_header,
                                      update_user=username,
                                      set_mock=mock, skip=skip)
                interface.save()
                log.info(
                    'add interface  {}  success.  interface info： {} // {} // {} // {} // {} // {} // {} // {} // {} // {} '
                        .format(if_name, project, url, method, data_type, is_sign, description, request_header_param,
                                request_body_param, response_header_param, response_body_param, is_header))
                return HttpResponseRedirect("base/interface/")

    def interface_search(request):
        """
        接口搜索功能
        :param request:
        :return:
        """
        if request.method == 'POST':
            user_id = request.session.get('user_id', '')
            if get_user(user_id):
                search = request.POST.get('search', '').strip()
                if_list = []
                interface_list = []
                if not search:
                    return HttpResponse('0')
                else:
                    if search in ['get', 'post', 'delete', 'put']:  # 请求方式查询
                        interface_list = Interface.objects.filter(method__contains=search)
                    elif search in ['data', 'json']:  # 数据传输类型查询
                        interface_list = Interface.objects.filter(data_type__contains=search)
                    else:
                        try:
                            if isinstance(int(search), int):
                                if search in ['0', '1']:  # 设置header、签名查询
                                    interface_list = Interface.objects.filter(
                                        Q(is_header=search) | Q(is_sign=search) | Q(if_id__exact=search) | Q(
                                            if_name__contains=search))
                                else:  # ID查询
                                    interface_list = Interface.objects.filter(
                                        Q(if_id__exact=search) | Q(if_name__contains=search))
                        except ValueError:
                            interface_list = Interface.objects.filter(
                                Q(if_name__contains=search) | Q(project__prj_name__contains=search))  # 接口名称、项目名称查询
                    if not interface_list:  # 查询为空
                        return HttpResponse('1')
                    else:
                        for interface in interface_list:
                            interface_dict = {'if_id': str(interface.if_id), 'if_name': interface.if_name,
                                              'project': interface.project.prj_name, 'method': interface.method,
                                              'data_type': interface.data_type, 'is_sign': interface.is_sign,
                                              'description': interface.description,
                                              'response_header_param': interface.response_header_param,
                                              'update_time': str(interface.update_time).split('.')[0],
                                              'update_user': interface.update_user}
                            if_list.append(interface_dict)
                        return HttpResponse(str(if_list))
            else:
                return HttpResponse('2')

    def interface_add(request):
        """
        添加接口
        :param request:
        :return:
        """
        user_id = request.session.get('user_id', '')
        if not get_user(user_id):
            request.session['login_from'] = '/base/interface/'
            return render(request, 'user/login_action.html')
        else:
            if request.method == 'POST':
                if_name = request.POST['if_name'].strip()
                prj_id = request.POST['prj_id']
                url = request.POST['url'].strip()
                method = request.POST.get('method', '')
                skip = request.POST.get('skip', '').strip()
                data_type = request.POST['data_type']
                is_sign = request.POST.get('is_sign', '')
                is_headers = request.POST.get('is_headers', '')
                mock = request.POST.get('mock', '')
                request_header_data = request.POST['request_header_data']
                request_body_data = request.POST['request_body_data']
                # response_header_data = request.POST['response_header_data']
                # response_body_data = request.POST['response_body_data']

                msg = interface_info_logic(if_name, url, method, is_sign, data_type, is_headers, request_header_data,
                                           request_body_data)

                if msg != 'ok':
                    log.error('interface add error：{}'.format(msg))
                    return HttpResponse(msg)
                description = request.POST['description']
                username = request.session.get('user', '')
                if is_headers == '1':
                    Interface.objects.filter(project_id=prj_id).filter(is_header=1).update(is_header=0)
                project = Project.objects.get(prj_id=prj_id)
                interface = Interface(if_name=if_name, url=url, project=project, method=method, data_type=data_type,
                                      is_sign=is_sign, description=description,
                                      request_header_param=request_header_data,
                                      request_body_param=request_body_data, is_header=is_headers, update_user=username,
                                      set_mock=mock, skip=skip)
                interface.save()
                log.info(
                    'add interface  {}  success.  interface info： {} // {} // {} // {} // {} // {} // {} // {} //  '
                        .format(if_name, project, url, method, data_type, is_sign, description, request_header_data,
                                request_body_data, is_headers))
                return HttpResponseRedirect("/base/interface/")
            elif request.method == 'GET':
                prj_list = Project.objects.all()
                model_list = limits_of_authority(user_id)
                info = {"prj_list": prj_list, "model_list": model_list}
                return render(request, "base/interface/add.html", info)

    def interface_update(request):
        """
        接口编辑
        :param request:
        :return:
        """
        user_id = request.session.get('user_id', '')
        if not get_user(user_id):
            request.session['login_from'] = '/base/interface/'
            return render(request, 'user/login_action.html')
        else:
            if request.method == 'POST':
                if_id = request.POST['if_id']
                if_name = request.POST['if_name'].strip()
                prj_id = request.POST['prj_id']
                url = request.POST['url'].strip()
                skip = request.POST['skip'].strip()
                method = request.POST.get('method', '')
                page = request.POST.get('page', '1')
                data_type = request.POST['data_type']
                is_sign = request.POST.get('is_sign', '')
                is_headers = request.POST.get('is_headers', '')
                mock = request.POST.get('mock', '')
                request_header_data_list = request.POST.get('request_header_data', [])
                request_header_data = interface_format_params(request_header_data_list)
                request_body_data_list = request.POST.get('request_body_data', [])
                request_body_data = interface_format_params(request_body_data_list)
                # response_header_data_list = request.POST.get('response_header_data', [])
                # response_header_data = interface_format_params(response_header_data_list)
                # response_body_data_list = request.POST.get('response_body_data', [])
                # response_body_data = interface_format_params(response_body_data_list)

                msg = interface_info_logic(if_name, url, method, is_sign, data_type, is_headers, request_header_data,
                                           request_body_data, if_id)
                if msg != 'ok':
                    log.error('interface update error：{}'.format(msg))
                    return HttpResponse(msg)
                else:
                    description = request.POST['description']
                    username = request.session.get('user', '')
                    if is_headers == '1':
                        Interface.objects.filter(project_id=prj_id).filter(is_header=1).update(is_header=0)
                    project = Project.objects.get(prj_id=prj_id)
                    Interface.objects.filter(if_id=if_id).update(if_name=if_name, url=url, project=project,
                                                                 method=method,
                                                                 data_type=data_type, is_header=is_headers,
                                                                 is_sign=is_sign, description=description,
                                                                 request_header_param=request_header_data, skip=skip,
                                                                 request_body_param=request_body_data, set_mock=mock,
                                                                 update_time=datetime.now(), update_user=username)
                    log.info(
                        'edit interface  {}  success.  interface info： {} // {} // {} // {} // {} // {} // {} // {} // {} '.format(
                            if_name, project, url, method, data_type, is_sign, description, request_header_data,
                            request_body_data, is_headers))
                    return HttpResponse("ok")
            elif request.method == 'GET':
                prj_list = Project.objects.all()
                if_id = request.GET['if_id']
                page = request.GET['page']
                interface = Interface.objects.get(if_id=if_id)
                request_header_param_list = interface_get_params(interface.request_header_param)
                request_body_param_list = interface_get_params(interface.request_body_param)
                # response_header_param_list = interface_get_params(interface.response_header_param)
                # response_body_param_list = interface_get_params(interface.response_body_param)
                method, is_sign, is_headers, mock = format_params(interface)
                model_list = limits_of_authority(user_id)
                info = {"interface": interface, 'request_header_param_list': request_header_param_list,
                        'request_body_param_list': request_body_param_list, 'method': method, 'is_sign': is_sign,
                        'is_headers': is_headers, 'mock': mock, "prj_list": prj_list, "model_list": model_list,
                        "page": page}
                return render(request, "base/interface/update.html", info)

    def interface_get_params(params):
        """
        解析数据库中格式化前的参数
        :param params:
        :return:
        """
        if params and params != '[]':
            param_list = []
            for i in range(len(eval(params))):
                param_list.append({"var_name": "", "var_remark": ""})
                param_list[i]['var_name'] = eval(params)[i]['var_name']
            return param_list
        else:
            return []

    def interface_format_params(params_list):
        """
        格式化存入数据库中的参数
        :param params_list:
        :return:
        """
        if params_list:
            var = []
            params_list = eval(params_list)
            for i in range(len(params_list)):
                var.append({"var_name": "", "var_remark": ""})
                var[i]['var_name'] = params_list[i]['var_name']
            return json.dumps(var)
        else:
            return []

    def interface_delete(request):
        """
        接口删除
        :param request:
        :return:
        """
        user_id = request.session.get('user_id', '')
        if not get_user(user_id):
            request.session['login_from'] = '/base/interface/'
            return render(request, 'user/login_action.html')
        else:
            if request.method == 'GET':
                if_id = request.GET['if_id']
                page = request.GET.get("page", "1")
                interface = Interface.objects.filter(if_id=if_id)
                interface.delete()
                is_page = interface.count() % 10
                if not is_page and int(page) > 1:
                    page = int(page) - 1
                log.info('用户 {} 删除接口 {} 成功.'.format(user_id, if_id))
                return HttpResponseRedirect("base/interface/?page={}".format(page))
