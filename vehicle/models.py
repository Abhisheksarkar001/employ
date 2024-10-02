from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth import settings

# Create your models here.

class VehicleMaster(models.Model):

    class VehicleType(models.IntegerChoices):
        CAR = 1, 'Car'
        BUS = 2, 'Bus'

    class VehicleStatus(models.IntegerChoices):
        DISPOSE_OFF = 1, 'Dispose off'
        IN_STOCK = 2, 'In Stock'
        RUNNING = 3, 'Running'
        MAINTENANCE = 4, 'Maintenance'

        
    objects = models.Manager()
    vehicle_type = models.IntegerField(choices=VehicleType.choices, default=VehicleType.CAR)
    purchase_date = models.DateField(default=datetime.now, editable=False)
    bill_no = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    road_permit_date = models.DateField(default=datetime.now, editable=False)
    road_tax_date = models.DateField(default=datetime.now, editable=False)
    pollution_date = models.DateField(default=datetime.now, editable=False)
    insurance_date = models.DateField(default=datetime.now, editable=False)
    status = models.IntegerField(choices=VehicleStatus.choices, default=VehicleStatus.IN_STOCK)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        editable=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.get_vehicle_type_display()
    class Meta:
        """doc string here"""
        verbose_name_plural = "VehicleMaster"
        verbose_name = "VehicleMaster"



class VehicleJourneyDetail(models.Model):
    class UseType(models.IntegerChoices):
        OFFICIAL = 1, 'Official'
        PERSONAL = 2, 'Personal'
    
    class UsedBy(models.IntegerChoices):
        MANAGEMENT = 1, 'Management'
        EMPLOYEE = 2, 'Employee'
        STUDENT = 3, 'Student'
    
    objects = models.Manager()
    vehicle_no = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=50)
    journey_detail = models.TextField()
    start_journey_km = models.IntegerField(default=0)
    end_journey_km = models.IntegerField(default=0)
    total_km = models.IntegerField(default=0)
    use_type = models.IntegerField(choices=UseType.choices)
    used_by = models.IntegerField(choices=UsedBy.choices)
    user_name_with_id = models.CharField(max_length=100)
    user_mo_no = models.CharField(max_length=15)
    driver_name_with_id = models.CharField(max_length=100)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        editable=False,
        null=True,
        blank=True,
    )
    approved_by = models.CharField(max_length=100)

    def __str__(self):
        return str(self.vehicle_no)

    class Meta:
        """doc string here"""
        verbose_name_plural = "VehicleJourneyDetail"
        verbose_name = "VehicleJourneyDetail"


class VehicleFuelRequisition(models.Model):
    FUEL_TYPE_CHOICES = [
        ('Diesel', 'Diesel'),
        ('Petrol', 'Petrol'),
        ('CNG', 'CNG'),
    ]
    

    objects = models.Manager()
    vehicle_no = models.CharField(max_length=100)
    today_fuel_filling_date = models.DateField(default=datetime.now, editable=False)
    previous_fuel_filling_date = models.DateField(default=datetime.now, editable=False)
    previous_vehicle_reading_km = models.IntegerField(default=0)
    previous_fuel_rate = models.DecimalField(max_digits=5, decimal_places=2)
    previous_fuel_qty = models.DecimalField(max_digits=5, decimal_places=2)
    today_vehicle_reading_km = models.IntegerField(default=0)
    net_journey_km = models.IntegerField(default=0)
    fuel_average = models.DecimalField(max_digits=5, decimal_places=2)
    fuel_type = models.CharField(max_length=50, choices=FUEL_TYPE_CHOICES)
    today_required_qty_lt = models.DecimalField(max_digits=5, decimal_places=2)
    fuel_rate = models.DecimalField(max_digits=5, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bill_no = models.CharField(max_length=100)
    requested_by_driver = models.CharField(max_length=100)
    approved_by_in_charge = models.CharField(max_length=100)


    def __str__(self):
        return str(self.vehicle_no)
    class Meta:
        """doc string here"""
        verbose_name_plural = "VehicleFuelRequisition"
        verbose_name = "VehicleFuelRequisition"


class VehicleMaintenanceRecord(models.Model):

    
    objects = models.Manager()
    vehicle_no = models.CharField(max_length=100)
    date = models.DateField(default=datetime.now, editable=False)
    vehicle_reading = models.IntegerField(default=0)
    bill_no = models.CharField(max_length=100)
    bill_amount = models.DecimalField(max_digits=10, decimal_places=2)
    service_provider_name = models.CharField(max_length=100)
    service_provider_mo_no = models.CharField(max_length=15)
    maintenance_detail = models.TextField()
    requested_by_driver = models.CharField(max_length=100)
    approved_by_in_charge = models.CharField(max_length=100)


    def __str__(self):
        return str(self.vehicle_no)
    class Meta:
        """doc string here"""
        verbose_name_plural = "VehicleMaintenanceRecord"
        verbose_name = "VehicleMaintenanceRecord"