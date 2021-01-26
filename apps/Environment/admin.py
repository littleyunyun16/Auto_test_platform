from django.contrib import admin
from .models import Environment


class EnvAdmin(admin.ModelAdmin):
    list_display = ["env_id", "env_name", "project", "url", "is_swagger", "private_key", "update_user", "update_time"]
    list_filter = ["update_time"]
    search_fields = ["env_name", "update_user"]


admin.site.register(Environment, EnvAdmin)

