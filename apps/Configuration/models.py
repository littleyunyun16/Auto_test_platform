from django.db import models
from django.contrib.auth.models import User


class UserPower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    power = models.CharField(max_length=255)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "用户权限"
        verbose_name_plural = "用户权限"
