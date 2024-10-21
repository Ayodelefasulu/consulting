from django.contrib import admin
from .models import Business

# Register your models here.
#admin.site.register(Business)

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ['business_name', 'username', 'created', 'industry', 'type_of_service', 'deadline']
    list_filter = ['username', 'created', 'deadline', 'business_name']
    search_fields = ['business_name', 'type_of_service', 'industry']
    raw_id_fields = ['username']
    date_hierarchy = 'created'
    ordering = ['deadline', 'created', 'industry']
    show_facets = admin.ShowFacets.ALWAYS
