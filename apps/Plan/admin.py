from django.contrib import admin
from .models import  Plan


class PlanAdmin(admin.ModelAdmin):
    list_display = ["plan_id", "plan_name", "project", "environment", "is_locust", "is_task", "content", "update_user",
                    "update_time"]
    list_filter = ["update_time"]
    search_fields = ["plan_name", "update_user"]


admin.site.register(Plan, PlanAdmin)

