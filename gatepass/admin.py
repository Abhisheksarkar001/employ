from django.contrib import admin
from .models import GatePass


# Register your models here.
class GatePassAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'date', 'time', 'pass_type', 'parent_approval', 'approved_by')
    search_fields = ('student_id', 'student_mo_no')
    list_filter = ('pass_type', 'parent_approval', 'date')

    def save_model(self, request, obj, form, change):
        if not change:  
            obj.approved_by = request.user  
        super().save_model(request, obj, form, change)

admin.site.register(GatePass, GatePassAdmin)
