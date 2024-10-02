from django.contrib import admin
from .models import AssetsRecord, IssueReturn, AssetsMaintenanceRecord
from django.utils.timezone import now


class AssetsRecordAdmin(admin.ModelAdmin):
    list_display = ('fixed_assets_no', 'name', 'category', 'status', 'purchase_date')
    search_fields = ('name', 'fixed_assets_no', 'vendor_name')
    list_filter = ('status', 'category')

    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.created_by = request.user  
        super().save_model(request, obj, form, change)


class IssueReturnAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'issue_return_status', 'issue_request_datetime', 'return_datetime')
    search_fields = ('employee_id', 'name')
    list_filter = ('issue_return_status', 'item_status')

    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.created_by = request.user  
        super().save_model(request, obj, form, change)


class AssetsMaintenanceRecordAdmin(admin.ModelAdmin):
    list_display = ('asset_no', 'service_provider_name', 'bill_amount', 'date')
    search_fields = ('asset_no', 'service_provider_name')
    list_filter = ('date',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.created_by = request.user  
        super().save_model(request, obj, form, change)


# Register the models in the Django admin
admin.site.register(AssetsRecord, AssetsRecordAdmin)
admin.site.register(IssueReturn, IssueReturnAdmin)
admin.site.register(AssetsMaintenanceRecord, AssetsMaintenanceRecordAdmin)
