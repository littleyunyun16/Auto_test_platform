from django.contrib import admin
from .models import  Case

class CaseAdmin(admin.ModelAdmin):
    list_display = ["case_id", "case_name", "project", "description", "update_user", "update_time"]
    list_filter = ["update_time"]
    search_fields = ["env_name", "update_user"]

admin.site.register(Case, CaseAdmin)
