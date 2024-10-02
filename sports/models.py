from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth import settings

# Create your models here.


class SportsAssets(models.Model):
    SPORTS_TYPE_CHOICES = [
        (1, 'Indoor'),
        (2, 'Outdoor'),
    ]
    STATUS_CHOICES = [
        (1, 'In Stock'),
        (2, 'Dispose off'),
        (3, 'Issued'),
        (4, 'Maintenance'),
    ]
    

    objects = models.Manager()
    sports_asst_no = models.CharField(max_length=50)
    assets_name = models.CharField(max_length=100)
    model_no = models.CharField(max_length=50)
    game_name = models.CharField(max_length=100)
    assets_type = models.CharField(max_length=10, choices=SPORTS_TYPE_CHOICES)
    purchase_date = models.DateField(default=datetime.now, null=True, blank=True, editable=False)
    warranty_duration = models.IntegerField(default=0)  
    brand_name = models.CharField(max_length=100)
    bill_no = models.CharField(max_length=50, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    vendor_name = models.CharField(max_length=100)
    vendor_mo_no = models.CharField(max_length=15)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        editable=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.assets_name)
    class Meta:
        """doc string here"""
        verbose_name_plural = "SportsAssets"
        verbose_name = "SportsAssets"


class IssueReturn(models.Model):
    ISSUE_RETURN_STATUS_CHOICES = [
        (1, 'Issue'),
        (2, 'Return'),
    ]
    ITEM_STATUS_CHOICES = [
        (1, 'Ok'),
        (2, 'Damage'),
    ]
    

    objects = models.Manager()
    student_code = models.CharField(max_length=50)
    sports_assets_no = models.ForeignKey(SportsAssets, on_delete=models.CASCADE)
    issue_date_time = models.DateField(default=datetime.now, null=True, blank=True, editable=False)
    return_date_time = models.DateField(default=datetime.now, null=True, blank=True, editable=False)
    issue_return_status = models.CharField(max_length=10, choices=ISSUE_RETURN_STATUS_CHOICES)
    sports_item_status = models.CharField(max_length=10, choices=ITEM_STATUS_CHOICES)
    sports_fine = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        editable=False,
        null=True,
        blank=True,
    )
    approved_by = models.CharField(max_length=50)

    def __str__(self):
        return str(self.student_code)
    class Meta:
        """doc string here"""
        verbose_name_plural = "IssueReturn"
        verbose_name = "IssueReturn"


class MaintenanceRecord(models.Model):

    objects = models.Manager()
    sports_assets_no = models.ForeignKey(SportsAssets, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now, null=True, blank=True, editable=False)
    bill_no = models.CharField(max_length=50, blank=True, null=True)
    bill_amount = models.DecimalField(max_digits=10, decimal_places=2)
    service_provider_name = models.CharField(max_length=100)
    service_provider_mo_no = models.CharField(max_length=15)
    maintenance_detail = models.TextField(null=True, blank=True)
    created_by = models.CharField(max_length=50)
    approved_by = models.CharField(max_length=50)

    def __str__(self):
        return str(self.sports_assets_no)
    class Meta:
        """doc string here"""
        verbose_name_plural = "MaintenanceRecord"
        verbose_name = "MaintenanceRecord"