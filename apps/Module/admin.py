# Register your models here.
from django.contrib import admin
from apps.Module.models import Product  # 把product引入到当前环境


class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'producter', 'create_time', 'id']
    search_fields = ['productname','producter']
    list_filter = ['productname']
    admin.site.register(Product)  # 把产品模块注册到 Django admin 后台并能显示

