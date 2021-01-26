from django.contrib import admin
from .models import Interface


class InterfaceAdmin(admin.ModelAdmin):
    list_display = ["if_id", "if_name", "project", "url", "method", "data_type", "is_sign", "is_header", "set_mock",
                    "update_user", "update_time"]
    list_filter = ["update_time"]
    search_fields = ["if_name", "update_user"]


admin.site.register(Interface, InterfaceAdmin)