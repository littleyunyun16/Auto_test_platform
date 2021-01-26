from django.db import models
from django.contrib.auth.models import User
from apps.Sign.models import Sign

class Project(models.Model):
    prj_id = models.AutoField(primary_key=True, null=False)
    prj_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    sign = models.ForeignKey(Sign, on_delete=models.CASCADE, default='')
    description = models.CharField(max_length=200)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.prj_name

    class Meta:
        verbose_name = "项目管理"
        verbose_name_plural = "项目管理"
