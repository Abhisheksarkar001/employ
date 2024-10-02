from django.contrib import admin
from .models import GensetMaster, GensetRunningDetail, GensetFuelRequisition, GensetMaintenanceRecord

# Register your models here.

class GensetMasterAdmin(admin.ModelAdmin):
    list_display = ('genset_no', 'kilowatt', 'purchase_date', 'amount', 'status', 'created_by')
    search_fields = ('genset_no', 'location')
    list_filter = ('status', 'kilowatt')

    def save_model(self, request, obj, form, change):
        if not obj.pk: 
            obj.created_by = request.user  
        super().save_model(request, obj, form, change)

class GensetRunningDetailAdmin(admin.ModelAdmin):
    list_display = ('genset_no', 'date', 'total_time', 'use_type', 'used_by_department', 'user_name', 'approved_by')
    search_fields = ('genset_no', 'user_name')
    list_filter = ('use_type', 'used_by_department')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user 
        super().save_model(request, obj, form, change)

class GensetFuelRequisitionAdmin(admin.ModelAdmin):
    list_display = ('genset_no', 'today_filling_date', 'previous_fuel_filling_date', 'total_running_hour', 'fuel_type', 'requested_by', 'approved_by_in_charge')
    search_fields = ('genset_no', 'requested_by')
    list_filter = ('fuel_type',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.requested_by = request.user.username  
        super().save_model(request, obj, form, change)


class GensetMaintenanceRecordAdmin(admin.ModelAdmin):
    list_display = ('genset_no', 'date', 'bill_no', 'bill_amount', 'service_provider_name', 'requested_by', 'approved_by_in_charge')
    search_fields = ('genset_no', 'service_provider_name')
    list_filter = ('date',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.requested_by = request.user.username  
        super().save_model(request, obj, form, change)


admin.site.register(GensetMaster, GensetMasterAdmin)
admin.site.register(GensetRunningDetail, GensetRunningDetailAdmin)
admin.site.register(GensetFuelRequisition, GensetFuelRequisitionAdmin)
admin.site.register(GensetMaintenanceRecord, GensetMaintenanceRecordAdmin)
