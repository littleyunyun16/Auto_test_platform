from django.db import models

class Sign(models.Model):
    sign_id = models.AutoField(primary_key=True, null=False)
    sign_name = models.CharField(max_length=100)
    sign_type = models.CharField(max_length=100, default="无")
    description = models.CharField(max_length=200)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    update_user = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.sign_name

    class Meta:
        verbose_name = "签名管理"
        verbose_name_plural = "签名管理"
