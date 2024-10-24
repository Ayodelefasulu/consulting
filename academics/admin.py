from django.contrib import admin
from .models import Academic

# Register your models here.
@admin.register(Academic)
class AcademicAdmin(admin.ModelAdmin):
    list_display = ['project_title', 'username', 'academic_level', 'name_of_institution', 'type_of_service', 'created', 'deadline', 'status']
    list_filter = ['username', 'academic_level', 'created', 'deadline']
    list_per_page = 50
    search_fields = ['project_title', 'academic_level' 'type_of_service']
    raw_id_fields = ['username']
    date_hierarchy = 'created'
    ordering = ['academic_level', 'created', 'deadline', 'status']
    show_facets = admin.ShowFacets.ALWAYS
