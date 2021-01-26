from django.contrib import admin

from .models import  Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ["prj_id", "prj_name", "sign", "description", "user", "update_time"]
    list_filter = ["update_time"]
    search_fields = ["prj_name", "user"]


admin.site.register(Project, ProjectAdmin)

