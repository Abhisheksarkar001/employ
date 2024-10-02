from django.contrib import admin
from .models import VehicleMaster, VehicleJourneyDetail, VehicleFuelRequisition, VehicleMaintenanceRecord

class VehicleMasterAdmin(admin.ModelAdmin):
    list_display = ('vehicle_type', 'purchase_date', 'bill_no', 'amount', 'road_permit_date', 'road_tax_date', 'pollution_date', 'insurance_date', 'status', 'created_by')
    search_fields = ('vehicle_type', 'bill_no', 'status')
    list_filter = ('status', 'vehicle_type')
    
    def save_model(self, request, obj, form, change):
       
        if not obj.pk:  
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

class VehicleJourneyDetailAdmin(admin.ModelAdmin):
    list_display = ('vehicle_no', 'vehicle_type', 'journey_detail', 'start_journey_km', 'end_journey_km', 'total_km', 'use_type', 'used_by', 'user_name_with_id', 'driver_name_with_id', 'created_by', 'approved_by')
    search_fields = ('vehicle_no', 'use_type', 'used_by')
    list_filter = ('use_type', 'used_by')
    
    def save_model(self, request, obj, form, change):
        
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

class VehicleFuelRequisitionAdmin(admin.ModelAdmin):
    list_display = ('vehicle_no', 'today_fuel_filling_date', 'previous_fuel_filling_date', 'previous_vehicle_reading_km', 'fuel_type', 'today_required_qty_lt', 'fuel_rate', 'amount', 'requested_by_driver', 'approved_by_in_charge')
    search_fields = ('vehicle_no', 'fuel_type', 'requested_by_driver')
    list_filter = ('fuel_type',)
    
    def save_model(self, request, obj, form, change):
        
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

class VehicleMaintenanceRecordAdmin(admin.ModelAdmin):
    list_display = ('vehicle_no', 'date', 'vehicle_reading', 'bill_no', 'bill_amount', 'service_provider_name', 'service_provider_mo_no', 'maintenance_detail', 'requested_by_driver', 'approved_by_in_charge')
    search_fields = ('vehicle_no', 'service_provider_name', 'requested_by_driver')
    list_filter = ('date',)
    
    def save_model(self, request, obj, form, change):
        
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(VehicleMaster, VehicleMasterAdmin)
admin.site.register(VehicleJourneyDetail, VehicleJourneyDetailAdmin)
admin.site.register(VehicleFuelRequisition, VehicleFuelRequisitionAdmin)
admin.site.register(VehicleMaintenanceRecord, VehicleMaintenanceRecordAdmin)
