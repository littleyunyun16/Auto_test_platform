from django.db import models
from django.contrib.auth.models import User

class ModularTable(models.Model):
    url = models.CharField(max_length=255)
    Icon = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255)

    def __str__(self):
        return self.model_name

    class Meta:
        verbose_name = "模块名称"
        verbose_name_plural = "模块名称"


class UserPower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    power = models.CharField(max_length=255)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "用户权限"
        verbose_name_plural = "用户权限"
