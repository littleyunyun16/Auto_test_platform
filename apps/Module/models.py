from django.db import models

# Create your models here.

from django.db import models


class ModularTable(models.Model):
    url = models.CharField(max_length=255)
    Icon = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255)

    def __str__(self):
        return self.model_name

    class Meta:
        verbose_name = "模块名称"
        verbose_name_plural = "模块名称"

