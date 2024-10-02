from django.contrib import admin
from .models import SportsAssets, IssueReturn, MaintenanceRecord
from django.utils.timezone import now

class SportsAssetsAdmin(admin.ModelAdmin):
    list_display = ('sports_asst_no', 'assets_name', 'assets_type', 'status', 'purchase_date')
    search_fields = ('assets_name', 'sports_asst_no', 'game_name')
    list_filter = ('status', 'assets_type')

    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

class IssueReturnAdmin(admin.ModelAdmin):
    list_display = ('student_code', 'sports_assets_no', 'issue_return_status', 'issue_date_time', 'return_date_time')
    search_fields = ('student_code', 'sports_assets_no__assets_name')
    list_filter = ('issue_return_status', 'sports_item_status')

    def save_model(self, request, obj, form, change):
        if not obj.pk: 
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

class MaintenanceRecordAdmin(admin.ModelAdmin):
    list_display = ('sports_assets_no', 'service_provider_name', 'bill_amount', 'date')
    search_fields = ('sports_assets_no__assets_name', 'service_provider_name')
    list_filter = ('date',)

    def save_model(self, request, obj, form, change):
        if not obj.pk: 
            obj.created_by = request.user.username
        super().save_model(request, obj, form, change)


admin.site.register(SportsAssets, SportsAssetsAdmin)
admin.site.register(IssueReturn, IssueReturnAdmin)
admin.site.register(MaintenanceRecord, MaintenanceRecordAdmin)
