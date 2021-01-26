from django.db import models
from apps.Project.models import Project

class Interface(models.Model):
    if_id = models.AutoField(primary_key=True, null=False)
    if_name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    method = models.CharField(max_length=10)
    data_type = models.CharField(max_length=10)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    is_sign = models.IntegerField()
    is_header = models.IntegerField(default=0)  # 标记设置header接口
    set_mock = models.TextField(default='')  # 设置mock
    skip = models.TextField(default='')  # 跳过
    description = models.CharField(max_length=200)
    request_header_param = models.TextField()
    request_body_param = models.TextField()
    response_header_param = models.TextField()
    response_body_param = models.TextField()
    update_time = models.DateTimeField('更新时间', auto_now=True)
    update_user = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.if_name

    class Meta:
        verbose_name = "接口管理"
        verbose_name_plural = "接口管理"