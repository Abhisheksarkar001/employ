from django.contrib import admin
from .models import VisitorRegister, AppointmentRegister

# Register your models here.

class VisitorRegisterAdmin(admin.ModelAdmin):
    list_display = (
        'visitor_type', 
        'visitor_mobile', 
        'name', 
        'visit_purpose', 
        'in_date_time', 
        'out_date_time', 
        'token_no'
    )
    search_fields = ('name', 'visitor_mobile', 'visit_purpose')
    list_filter = ('visitor_type', 'whom_to_meet')


class AppointmentRegisterAdmin(admin.ModelAdmin):
    list_display = (
        'appointee_type', 
        'name', 
        'mo_no', 
        'appointment_date', 
        'appointment_time', 
        'appointment_status'
    )
    search_fields = ('name', 'mo_no', 'purpose')
    list_filter = ('appointee_type', 'appointment_status', 'appointment_date')


admin.site.register(VisitorRegister, VisitorRegisterAdmin)
admin.site.register(AppointmentRegister, AppointmentRegisterAdmin)