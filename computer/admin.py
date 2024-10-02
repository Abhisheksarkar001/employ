# admin.py
from django.contrib import admin
from .models import ITAssetRecord, AssetType, AssetMaintenanceRecord, IssueReturnRecord

class ITAssetRecordAdmin(admin.ModelAdmin):
    list_display = ('asset_no', 'name', 'category', 'purchase_date', 'status')
    search_fields = ('asset_no', 'name', 'model_no')
    list_filter = ('status', 'category')

    def save_model(self, request, obj, change):

        super().save_model(request, obj, change)

class AssetTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    def save_model(self, request, obj, change):
        
        super().save_model(request, obj, change)

class AssetMaintenanceRecordAdmin(admin.ModelAdmin):
    list_display = ('it_asset', 'name', 'date', 'bill_amount')
    search_fields = ('name', 'it_asset__name')
    list_filter = ('date',)

    def save_model(self, request, obj, change):
        
        super().save_model(request, obj, change)

class IssueReturnRecordAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'it_asset', 'issue_request_date_time', 'issue_date_time', 'return_date_time')
    search_fields = ('employee_id', 'it_asset__name')
    list_filter = ('item_status',)

    def save_model(self, request, obj, change):
       
        super().save_model(request, obj, change)

# Register the models with the admin site
admin.site.register(ITAssetRecord, ITAssetRecordAdmin)
admin.site.register(AssetType, AssetTypeAdmin)
admin.site.register(AssetMaintenanceRecord, AssetMaintenanceRecordAdmin)
admin.site.register(IssueReturnRecord, IssueReturnRecordAdmin)
