from django.db import models
from apps.Project.models import Project
from apps.Environment.models import Environment

class Plan(models.Model):
    plan_id = models.AutoField(primary_key=True, null=False)
    plan_name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    content = models.TextField()
    report_name = models.CharField(max_length=255, default="")
    make = models.IntegerField(null=True)
    is_locust = models.IntegerField(default=0)  # 性能测试
    is_task = models.IntegerField(default=0)  # 定时任务
    update_time = models.DateTimeField('更新时间', auto_now=True)
    update_user = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.plan_name

    class Meta:
        verbose_name = "测试计划"
        verbose_name_plural = "测试计划"
