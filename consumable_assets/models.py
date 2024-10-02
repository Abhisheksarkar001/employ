from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth import settings

# Create your models here.

class ConsumableAsset(models.Model):
    con_assets_no = models.CharField(max_length=100)  
    name = models.CharField(max_length=255)  
    marker = models.CharField(max_length=100)  
    cartage = models.DecimalField(max_digits=10, decimal_places=2)  
    quantity_as_on_date = models.IntegerField(default=0)  

    def __str__(self):
        return str(self.name)
    class Meta:
        """doc string here"""
        verbose_name_plural = "ConsumableAsset"
        verbose_name = "ConsumableAsset"

class AssetsType(models.Model):

    objects = models.Manager()
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)
    class Meta:
        """doc string here"""
        verbose_name_plural = "AssetsType"
        verbose_name = "AssetsType"


class PurchaseRegister(models.Model):
    con_assets_no = models.ForeignKey(ConsumableAsset, on_delete=models.CASCADE)  
    name = models.CharField(max_length=255)  
    purchase_date = models.DateField(default=datetime.now, null=True, blank=True, editable=False)
    bill_no = models.CharField(max_length=100)  
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    vendor_name = models.CharField(max_length=255, blank=True, null=True)  
    vendor_mo_no = models.CharField(max_length=15, blank=True, null=True)  
    quantity = models.IntegerField()  
    created_by = models.CharField(max_length=100)  

    def __str__(self):
        return str(self.name)
    class Meta:
        """doc string here"""
        verbose_name_plural = "PurchaseRegister"
        verbose_name = "PurchaseRegister"


class IssueRegister(models.Model):
    con_assets_no = models.ForeignKey(ConsumableAsset, on_delete=models.CASCADE)  
    employee_id = models.CharField(max_length=100)  
    issue_date = models.DateField()  
    issue_to = models.CharField(max_length=255)  
    quantity = models.PositiveIntegerField()  
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        editable=False,
        null=True,
        blank=True,
    )  
    approved_by = models.CharField(max_length=100)  

    def __str__(self):
        return str(self.employee_id)
    class Meta:
        """doc string here"""
        verbose_name_plural = "IssueRegister"
        verbose_name = "IssueRegister"