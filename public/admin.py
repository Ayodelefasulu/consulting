from django.contrib import admin
from .models import Public

# Register your models here.

@admin.register(Public)
class PublicAdmin(admin.ModelAdmin):
    list_display = ['project_title', 'username', 'category', 'type_of_service', 'created', 'deadline', 'status']
    list_filter = ['username', 'category', 'created', 'deadline']
    list_per_page = 50
    search_fields = ['category', 'type_of_service']
    raw_id_fields = ['username']
    date_hierarchy = 'created'
    ordering = ['category', 'created', 'deadline', 'status']
    show_facets = admin.ShowFacets.ALWAYS

