from django.contrib import admin

from .models import  Report

class ReportAdmin(admin.ModelAdmin):
    list_display = ["report_id", "report_name", "totalTime", "startTime", "plan", "case_num", "pass_num", "fail_num",
                    "error_num", "make", "update_user", "update_time"]
    list_filter = ["update_time"]
    search_fields = ["report_name", "update_user", "make"]


admin.site.register(Report, ReportAdmin)
