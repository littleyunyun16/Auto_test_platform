from django.db import models
from apps.Project.models import Project
class Case(models.Model):
    case_id = models.AutoField(primary_key=True, null=False)
    case_name = models.CharField(max_length=100)
    weight = models.IntegerField(default=1)  # 权重
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    content = models.TextField()
    update_time = models.DateTimeField('更新时间', auto_now=True)
    update_user = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.case_name

    class Meta:
        verbose_name = "测试用例"
        verbose_name_plural = "测试用例"
