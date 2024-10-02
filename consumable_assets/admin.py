from django.contrib import admin
from .models import ConsumableAsset, AssetsType, PurchaseRegister, IssueRegister

class ConsumableAssetAdmin(admin.ModelAdmin):
    list_display = ('con_assets_no', 'name', 'marker', 'cartage', 'quantity_as_on_date')
    search_fields = ('name', 'con_assets_no')

    def save_model(self, request, obj, form, change):
        
        super().save_model(request, obj, form, change)

class AssetsTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    def save_model(self, request, obj, form, change):
        
        super().save_model(request, obj, form, change)

class PurchaseRegisterAdmin(admin.ModelAdmin):
    list_display = ('con_assets_no', 'name', 'purchase_date', 'bill_no', 'amount', 'vendor_name', 'quantity')
    search_fields = ('name', 'bill_no', 'vendor_name')

    def save_model(self, request, obj, form, change):
        
        super().save_model(request, obj, form, change)

class IssueRegisterAdmin(admin.ModelAdmin):
    list_display = ('con_assets_no', 'employee_id', 'issue_date', 'issue_to', 'quantity', 'approved_by')
    search_fields = ('employee_id', 'issue_to')

    def save_model(self, request, obj, form, change):
        
        super().save_model(request, obj, form, change)

# Register your models with the admin site
admin.site.register(ConsumableAsset, ConsumableAssetAdmin)
admin.site.register(AssetsType, AssetsTypeAdmin)
admin.site.register(PurchaseRegister, PurchaseRegisterAdmin)
admin.site.register(IssueRegister, IssueRegisterAdmin)
