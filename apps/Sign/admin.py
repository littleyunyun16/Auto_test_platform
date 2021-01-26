from django.contrib import admin
from .models import Sign


class SignAdmin(admin.ModelAdmin):
    list_display = ["sign_id", "sign_name", "description", "update_user", "update_time"]
    list_filter = ["update_time"]
    search_fields = ["sign_name", "update_user"]



admin.site.register(Sign, SignAdmin)
