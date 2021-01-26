from django.db import models
from apps.Plan.models import Plan

from celery import schedules
from celery import states
from celery.events.state import heartbeat_expires
from djcelery.models import PeriodicTask


class Report(models.Model):
    report_id = models.AutoField(primary_key=True, null=False)
    report_name = models.CharField(max_length=255)
    report_path = models.CharField(max_length=255, default='', null=True)
    pic_name = models.CharField(max_length=255, default='')
    totalTime = models.CharField(max_length=50, default='')
    startTime = models.CharField(max_length=50, default='')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)
    task = models.ForeignKey(PeriodicTask, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    case_num = models.IntegerField(null=True)
    skip_num = models.IntegerField(null=True)
    pass_num = models.IntegerField(null=True)
    fail_num = models.IntegerField(null=True)
    error_num = models.IntegerField(null=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    update_user = models.CharField(max_length=30, default='')
    make = models.IntegerField(null=True)

    def __str__(self):
        return self.report_name

    class Meta:
        verbose_name = "测试报告"
        verbose_name_plural = "测试报告"
