from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth import get_user_model

# Create your models here.


class VisitorRegister(models.Model):
    VISITOR_TYPE_CHOICES = [
        ('Student', 'Student'),
        ('Parent', 'Parent'),
        ('Govt/Company Official', 'Govt/Company Official'),
        ('Alumni', 'Alumni'),
    ]

    WHOM_TO_MEET_CHOICES = [
        ('Director', 'Director'),
        ('Principal', 'Principal'),
        ('Admission In Charge', 'Admission In Charge'),
        ('Office', 'Office'),
    ]


    objects = models.Manager()

    visitor_type = models.CharField(max_length=50, choices=VISITOR_TYPE_CHOICES)
    visitor_mobile = models.CharField(max_length=15,) 
    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    visit_purpose = models.TextField()
    whom_to_meet = models.CharField(max_length=50, choices=WHOM_TO_MEET_CHOICES)
    in_date_time = models.DateField(default=datetime.now, null=True, blank=True)
    out_date_time = models.DateField(default=datetime.now, null=True, blank=True)
    token_no = models.CharField(max_length=50, unique=True) 

    def __str__(self):
        return f"{self.name} - {self.visitor_type}"

    class Meta:
        verbose_name = "Visitor Register"
        verbose_name_plural = "Visitor Registers"


class AppointmentRegister(models.Model):
    APPOINTEE_TYPE_CHOICES = [
        ('Student', 'Student'),
        ('Parent', 'Parent'),
        ('Govt/Company Official', 'Govt/Company Official'),
        ('Alumni', 'Alumni'),
    ]

    APPOINTMENT_STATUS_CHOICES = [
        ('Request sent for Approval', 'Request sent for Approval'),
        ('Approved', 'Approved'),
        ('Cancel Appointment', 'Cancel Appointment'),
    ]
    

    objects = models.Manager()
    appointee_type = models.CharField(max_length=50, choices=APPOINTEE_TYPE_CHOICES)
    request_date = models.DateField(default=datetime.now, null=True, blank=True)
    name = models.CharField(max_length=100)
    mo_no = models.CharField(max_length=15,) 
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    appointment_date = models.DateField(default=datetime.now, null=True, blank=True)
    appointment_time = models.TimeField()
    purpose = models.TextField()
    appointment_to_whom = models.CharField(max_length=50, choices=[
        ('Director', 'Director'),
        ('Principal', 'Principal'),
    ])
    appointment_status = models.CharField(max_length=50, choices=APPOINTMENT_STATUS_CHOICES)

    def __str__(self):
        return str(self.appointee_type)

    class Meta:
        verbose_name = "Appointment Register"
        verbose_name_plural = "Appointment Registers"