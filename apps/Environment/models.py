from django.db import models
from apps.Project.models import Project

class Environment(models.Model):
    env_id = models.AutoField(primary_key=True, null=False)
    env_name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=100)
    import_url = models.CharField(max_length=100,default="")
    is_swagger = models.IntegerField(default=0)  # 导入swagger
    set_headers = models.TextField(default='')  # 设置默认headers
    private_key = models.CharField(max_length=100)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    update_user = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.env_name

    class Meta:
        verbose_name = "测试环境"
        verbose_name_plural = "测试环境"

