from django.contrib import admin
from .models import AssetsInOut

# Register your models here.


class AssetsInOutAdmin(admin.ModelAdmin):
    list_display = (
        'assets_no',
        'name',
        'out_date',
        'reason',
        'in_date',
        'technician_mo_no',
        'created_by',
        'approved_by',
    )
    search_fields = ('assets_no', 'name', 'reason', 'created_by__username', 'approved_by')
    list_filter = ('out_date', 'in_date')
    

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

admin.site.register(AssetsInOut, AssetsInOutAdmin)
