from django.contrib import admin

# Register your models here.


from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Book

@admin.register(Book)

class BookAdmin(ImportExportModelAdmin):
    list_display = (
        'title',
        'adoption',
        'number',
        'initial_cost',
        'calculate_depreciation',
        'cost_begining_period',
        'depreciation_begining_period',
        'residual_value_begining',
        'price_end_period',
        'depreciation_end_period',
        'residual_value'
        )
class header(admin.ModelAdmin):
    admin.site.site_title = 'Панель администратора'
    admin.site.site_header = 'Панель администратора'
