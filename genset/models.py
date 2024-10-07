from django.db import models
from django.utils import timezone
from django.utils.timezone import datetime
from django.contrib.auth import settings

# Create your models here.

class GensetMaster(models.Model):
    class KilowattType(models.IntegerChoices):
        KVA_65 = 65, '65 KVA'
        KVA_85 = 85, '85 KVA'

    class GensetStatus(models.IntegerChoices):
        DISPOSE_OFF = 1, 'Dispose off'
        IN_STOCK = 2, 'In Stock'
        RUNNING = 3, 'Running'
        MAINTENANCE = 4, 'Maintenance'
    

    objects = models.Manager()
    genset_no = models.CharField(max_length=100)
    kilowatt = models.IntegerField(choices=KilowattType.choices, default=KilowattType.KVA_65)
    purchase_date = models.DateField(default=datetime.now, null=True, blank=True)
    bill_no = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100, null=True, blank=True)
    status = models.IntegerField(choices=GensetStatus.choices, default=GensetStatus.IN_STOCK)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.genset_no)

    class Meta:
        verbose_name_plural = "Genset Master"
        verbose_name = "Genset Master"



class GensetRunningDetail(models.Model):
    class UseType(models.IntegerChoices):
        OFFICIAL = 1, 'Official'
        PERSONAL = 2, 'Personal'

    class UsedByDepartment(models.IntegerChoices):
        LAW = 1, 'Law'
        MANAGEMENT = 2, 'Management'
    
    objects = models.Manager()
    genset_no = models.CharField(max_length=100)
    date = models.DateField(default=datetime.now, null=True, blank=True)
    detail_purpose = models.TextField()
    start_time = models.TimeField(default=timezone.now)
    off_time = models.TimeField(default=timezone.now)
    total_time = models.DecimalField(max_digits=5, decimal_places=2)
    use_type = models.IntegerField(choices=UseType.choices)
    used_by_department = models.IntegerField(choices=UsedByDepartment.choices)
    user_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    approved_by = models.CharField(max_length=100)

    def __str__(self):
        return str(self.genset_no)

    class Meta:
        verbose_name_plural = "Genset Running Detail"
        verbose_name = "Genset Running Detail"



class GensetFuelRequisition(models.Model):
    class FuelType(models.TextChoices):
        DIESEL = 'Diesel', 'Diesel'
        PETROL = 'Petrol', 'Petrol'
        CNG = 'CNG', 'CNG'
    
    objects = models.Manager()
    genset_no = models.CharField(max_length=100)
    today_filling_date = models.DateField(default=datetime.now, null=True, blank=True)
    previous_fuel_filling_date = models.DateField(default=datetime.now, null=True, blank=True)
    total_running_hour = models.DecimalField(max_digits=5, decimal_places=2)
    previous_fuel_rate = models.DecimalField(max_digits=5, decimal_places=2)
    previous_fuel_qty = models.DecimalField(max_digits=5, decimal_places=2)
    fuel_average_per_liter = models.DecimalField(max_digits=5, decimal_places=2)
    fuel_type = models.CharField(max_length=50, choices=FuelType.choices)
    today_required_qty_lt = models.DecimalField(max_digits=5, decimal_places=2)
    fuel_rate = models.DecimalField(max_digits=5, decimal_places=2)
    bill_no = models.CharField(max_length=100)
    requested_by = models.CharField(max_length=100)
    approved_by_in_charge = models.CharField(max_length=100)

    def __str__(self):
        return str(self.genset_no)

    class Meta:
        verbose_name_plural = "Genset Fuel Requisition"
        verbose_name = "Genset Fuel Requisition"



class GensetMaintenanceRecord(models.Model):


    objects = models.Manager()
    genset_no = models.CharField(max_length=100)
    date = models.DateField(default=datetime.now, null=True, blank=True)
    bill_no = models.CharField(max_length=100)
    bill_amount = models.DecimalField(max_digits=10, decimal_places=2)
    service_provider_name = models.CharField(max_length=100)
    service_provider_mo_no = models.CharField(max_length=15)
    maintenance_detail = models.TextField()
    requested_by = models.CharField(max_length=100)
    approved_by_in_charge = models.CharField(max_length=100)

    def __str__(self):
        return str(self.genset_no)

    class Meta:
        verbose_name_plural = "Genset Maintenance Record"
        verbose_name = "Genset Maintenance Record"
