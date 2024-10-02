from django.contrib import admin
from .models import PlacementRegister

# Register your models here.

class PlacementRegisterAdmin(admin.ModelAdmin):
    list_display = (
        'student_id', 
        'name', 
        'mo_no', 
        'status', 
        'placed_organization_name', 
        'salary_per_annum', 
        'placement_date'
    )
    search_fields = ('name', 'student_id', 'mo_no', 'placed_organization_name', 'father_name', 'mother_name')
    list_filter = ('status', 'category', 'religion', 'state', 'country', 'placement_date')

    def save_model(self, request, obj, form, change):
        if not change: 
            obj.created_by = request.user
        obj.save()


admin.site.register(PlacementRegister, PlacementRegisterAdmin)



