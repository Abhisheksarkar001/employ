from django.contrib import admin
from .models import VacancyRegister

# Register your models here.

class VacancyRegisterAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'vacancy_type', 
        'post', 
        'department', 
        'status'
    )
    search_fields = ('name', 'vacancy_type', 'post__designation_name', 'department__department_name')
    list_filter = ('vacancy_type', 'status', 'religion', 'category', 'state', 'country')

    def save_model(self, request, obj, form, change):
        if not change: 
            obj.created_by = request.user
        obj.save()


admin.site.register(VacancyRegister, VacancyRegisterAdmin)
