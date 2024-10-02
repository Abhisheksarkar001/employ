from django.contrib import admin
from .models import EmployTeskDetailReport, EmployLeaveApplication

# Admin class for EmployTeskDetailReport
class EmployTeskDetailReportAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'employ_id', 'assign_date', 'completed_date', 'status', 'ranking')
    list_filter = ('status', 'assign_date', 'completed_date')
    search_fields = ('task_name', 'employ_id', 'name')
    ordering = ('-assign_date',)

    # Save the model
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the object is being created
            obj.created_by = request.user.username
        obj.save()

# Admin class for EmployLeaveApplication
class EmployLeaveApplicationAdmin(admin.ModelAdmin):
    list_display = ('employ_id', 'apply_date', 'leave_from', 'leave_to', 'leave_status', 'approved_by')
    list_filter = ('leave_status', 'apply_date')
    search_fields = ('employ_id', 'leave_reason')
    ordering = ('-apply_date',)

    # Save the model
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the object is being created
            obj.created_by = request.user.username
        obj.save()

# Register the models
admin.site.register(EmployTeskDetailReport, EmployTeskDetailReportAdmin)
admin.site.register(EmployLeaveApplication, EmployLeaveApplicationAdmin)
