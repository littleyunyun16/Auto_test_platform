# -*- coding: utf-8 -*-
__author__ = 'amy'
__date__ = '2021/1/27 23:06'


def create_model(user_id):
    model = ModularTable.objects.all()
    if not model:
        model_dict = [{"id": 1, "url": "/base/project/", "Icon": "fa fa-product-hunt fa-fw", "model_name": "项目管理"},
                      {"id": 2, "url": "/base/env/", "Icon": "fa fa-envira fa-fw", "model_name": "测试环境"},
                      {"id": 3, "url": "/base/interface/", "Icon": "fa fa-pinterest-square fa-fw",
                       "model_name": "接口管理"},
                      {"id": 4, "url": "/base/case/", "Icon": "fa fa-suitcase fa-fw", "model_name": "用例管理"},
                      {"id": 5, "url": "/base/plan/", "Icon": "fa fa-book fa-fw", "model_name": "测试计划"},
                      {"id": 6, "url": "/base/task/", "Icon": "fa fa-tasks fa-fw", "model_name": "定时任务"},
                      {"id": 7, "url": "/base/report_page/", "Icon": "fa fa-bar-chart fa-fw", "model_name": "运行报告"},
                      {"id": 8, "url": "/base/performance/", "Icon": "fa fa-book fa-fw", "model_name": "性能测试"},
                      {"id": 9, "url": "/base/sign/", "Icon": "fa fa-pencil fa-fw", "model_name": "签名方式"},
                      {"id": 10, "url": "/base/user/", "Icon": "fa fa-user fa-fw", "model_name": "用户管理"},
                      {"id": 11, "url": "/base/about/", "Icon": "fa fa-cog fa-cab fa-fw", "model_name": "关于我们"}, ]
        for model_ in model_dict:
            model.create(id=model_["id"], url=model_["url"], Icon=model_["Icon"], model_name=model_["model_name"])
    user = UserPower.objects.filter(user_id=user_id)
    if not user:
        user.create(power=json.dumps(["10"]), user_id=user_id)
