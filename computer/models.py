from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth import settings

# Create your models here.

class ITAssetRecord(models.Model):

    STATUS_CHOICES = [
        (1, 'In Stock'),
        (2, 'Dispose off'),
        (3, 'Issued'),
        (4, 'Running'),
        (5, 'Maintenance'),
    ]
    
    object = models.Manager()
    asset_no = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='Electronic')
    purchase_date = models.DateField(default=datetime.now, null=True, blank=True)
    model_no = models.CharField(max_length=100)
    warranty_duration = models.CharField(max_length=50)
    bill_no = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    brand_name = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=100)
    vendor_phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)

    def __str__(self):
        return str(self.name)
    class Meta:
        """doc string here"""
        verbose_name_plural = "ITAssetRecord"
        verbose_name = "ITAssetRecord"
    
class AssetType(models.Model):

    objects = models.Manager()
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)
    class Meta:
        """doc string here"""
        verbose_name_plural = "AssetType"
        verbose_name = "AssetType"



class AssetMaintenanceRecord(models.Model):

    objects = models.Manager()
    it_asset = models.ForeignKey(ITAssetRecord, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField(default=datetime.now, null=True, blank=True)
    bill_no = models.CharField(max_length=100)
    bill_amount = models.DecimalField(max_digits=10, decimal_places=2)
    service_provider_name = models.CharField(max_length=100)
    service_provider_phone = models.CharField(max_length=15)
    maintenance_detail = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        editable=False,
        null=True,
        blank=True,
    )
    approved_by = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
    class Meta:
        """doc string here"""
        verbose_name_plural = "AssetMaintenanceRecord"
        verbose_name = "AssetMaintenanceRecord"

class IssueReturnRecord(models.Model):
    ITEM_STATUS_CHOICES = [
        (1, 'Ok'),
        (2, 'Damage'),
    ]
    
    objects = models.Manager()
    employee_id = models.CharField(max_length=50)
    it_asset = models.ForeignKey(ITAssetRecord, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    issue_request_date_time = models.DateField(default=datetime.now, null=True, blank=True)
    issue_date_time = models.DateField(default=datetime.now, null=True, blank=True)
    return_date_time = models.DateField(default=datetime.now, null=True, blank=True)
    issue_approval_by = models.CharField(max_length=100)
    return_approval_by = models.CharField(max_length=100)
    item_status = models.CharField(max_length=10, choices=ITEM_STATUS_CHOICES)

    def __str__(self):
        return str(self.name)
    class Meta:
        """doc string here"""
        verbose_name_plural = "Employs"
        verbose_name = "Employ"