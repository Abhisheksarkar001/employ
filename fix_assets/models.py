from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth import settings


# Create your models here.

class AssetsRecord(models.Model):
    CATEGORIES = [
        (1, 'Electric'),
        (2, 'Electronic'),
        (3, 'Furniture'),
    ]

    STATUS_CHOICES = [
        (1, 'In Stock'),
        (2, 'Dispose Off'),
        (3, 'Issued'),
        (4, 'Running'),
        (5, 'Maintenance'),
    ]

    objects = models.Manager()
    fixed_assets_no = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORIES,)
    purchase_date = models.DateField(default=datetime.now, null=True, blank=True, editable=False)
    model_no = models.CharField(max_length=50)
    warranty_duration = models.IntegerField(help_text="Warranty in months")
    bill_no = models.CharField(max_length=50)
    brand_name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    vendor_name = models.CharField(max_length=100)
    vendor_mo_no = models.CharField(max_length=15)  
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=1)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        editable=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.name)
    class Meta:
        """doc string here"""
        verbose_name_plural = "AssetsRecord"
        verbose_name = "AssetsRecord"
    

class AssetType(models.Model):

    object = models.Manager()
    name = models.CharField(max_length=200)


    def __str__(self):
        return str(self.name)
    class Meta:
        """doc string here"""
        verbose_name_plural = "AssetType"
        verbose_name = "AssetType"
    
class Department(models.Model):

    object = models.Manager()
    law = models.CharField(max_length=200)
    library = models.CharField(max_length=200)

    def __str__(self):
        return str(self.law)
    class Meta:
        """doc string here"""
        verbose_name_plural = "Department"
        verbose_name = "Department"



class AssetsMaintenanceRecord(models.Model):
 
    object = models.Manager()
    asset_no = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField(default=datetime.now, null=True, blank=True, editable=False)
    bill_no = models.CharField(max_length=50)
    bill_amount = models.DecimalField(max_digits=10, decimal_places=2)
    service_provider_name = models.CharField(max_length=100)
    service_provider_mo_no = models.CharField(max_length=15)  
    maintenance_detail = models.TextField(null=True, blank=True)
    requested_by = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)
    approval_by = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
    class Meta:
        """doc string here"""
        verbose_name_plural = "AssetsMaintenanceRecord"
        verbose_name = "AssetsMaintenanceRecord"
    

class IssueReturn(models.Model):
    ISSUE_RETURN_STATUS_CHOICES = [
        (1, 'Issue'),
        (2, 'Return'),
    ]

    ITEM_STATUS_CHOICES = [
        (1, 'Ok'),
        (2, 'Damage'),
        
    ]

    employee_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    issue_request_datetime = models.DateTimeField()
    issue_datetime = models.DateTimeField(null=True, blank=True)
    return_datetime = models.DateTimeField(null=True, blank=True)
    issue_return_status = models.CharField(max_length=10, choices=ISSUE_RETURN_STATUS_CHOICES, default=1)
    item_status = models.CharField(max_length=10, choices=ITEM_STATUS_CHOICES, default=1)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        editable=False,
        null=True,
        blank=True,
    )
    approval_by = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
    class Meta:
        """doc string here"""
        verbose_name_plural = "IssueReturn"
        verbose_name = "IssueReturn"

