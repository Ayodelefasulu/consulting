from django.contrib import admin
from .models import Business

# Register your models here.
#admin.site.register(Business)

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ['business_name', 'username', 'industry', 'type_of_service', 'created', 'deadline', 'status']
    #fields = ['username', 'business_name', 'industry', 'type_of_service', 'project_description', 'created', 'deadline']
    list_filter = ['username', 'business_name', 'created', 'deadline']
    list_per_page = 50
    search_fields = ['business_name', 'type_of_service', 'industry']
    raw_id_fields = ['username']
    date_hierarchy = 'created'
    ordering = ['industry', 'created', 'deadline', 'status']
    show_facets = admin.ShowFacets.ALWAYS
