# Register your models here.
from django.contrib import admin
from apps.Module.models import ModularTable  # 把product引入到当前环境


class ModelAdmin(admin.ModelAdmin):
    list_display = ["id", "url", "Icon", "model_name"]
    list_filter = ["model_name"]
    search_fields = ["model_name"]

admin.site.register(ModularTable, ModelAdmin)