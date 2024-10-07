from django.db import models
from django.utils.timezone import datetime

class VacancyRegister(models.Model):
    VACANCY_TYPE_CHOICES = [
        ('Teaching', 'Teaching'),
        ('Clerical', 'Clerical'),
        ('Marketing', 'Marketing'),
        ('Placement', 'Placement'),
        ('Technical', 'Technical'),
        ('Administration', 'Administration'),
        ('Supporting Staff', 'Supporting Staff'),
        ('HR', 'HR'),
    ]
    
    RELIGION_CHOICES = [
        ('Hindu', 'Hindu'),
        ('Muslim', 'Muslim'),
        ('Sikh', 'Sikh'),
        ('Christian', 'Christian'),
        ('Other', 'Other'),
    ]
    
    CATEGORY_CHOICES = [
        ('GEN', 'GEN'),
        ('SC', 'SC'),
        ('ST', 'ST'),
        ('OBC', 'OBC'),
        ('EWS', 'EWS'),
    ]
    
    STATUS_CHOICES = [
        ('In Process', 'In Process'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
        ('Eligible', 'Eligible'),
    ]
    

    objects = models.Manager()
    vacancy_type = models.CharField(max_length=50, choices=VACANCY_TYPE_CHOICES)
    post = models.ForeignKey('Designation', on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    
    name = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    mo_no_1 = models.CharField(max_length=15)
    mo_no_2 = models.CharField(max_length=15, blank=True, null=True)
    mail_id = models.EmailField(max_length=100)
    aadhaar_no = models.CharField(max_length=12)
    aadhaar_attach = models.FileField(upload_to='documents/', blank=True, null=True)
    pan_no = models.CharField(max_length=10, blank=True, null=True)
    pan_attach = models.FileField(upload_to='documents/', blank=True, null=True)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    dob = models.DateField(default=datetime.now, null=True, blank=True)
    religion = models.CharField(max_length=50, choices=RELIGION_CHOICES)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    address = models.TextField(null=True, blank=True)
    city_district = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
    high_school_name = models.CharField(max_length=100)
    high_school_subject = models.CharField(max_length=100)
    high_school_year = models.CharField(max_length=4)
    high_school_percent = models.CharField(max_length=10)
    high_school_attach = models.FileField(upload_to='documents/', blank=True, null=True)
    
    inter_name = models.CharField(max_length=100)
    inter_subject = models.CharField(max_length=100)
    inter_year = models.CharField(max_length=4)
    inter_percent = models.CharField(max_length=10)
    inter_attach = models.FileField(upload_to='documents/', blank=True, null=True)
    
    graduate_degree = models.CharField(max_length=100)
    graduate_college_name = models.CharField(max_length=100)
    graduate_subject = models.CharField(max_length=100)
    graduate_year = models.CharField(max_length=4)
    graduate_percent = models.CharField(max_length=10)
    graduate_attach = models.FileField(upload_to='documents/', blank=True, null=True)
    
    post_graduate_degree = models.CharField(max_length=100, blank=True, null=True)
    post_graduate_college_name = models.CharField(max_length=100, blank=True, null=True)
    post_graduate_subject = models.CharField(max_length=100, blank=True, null=True)
    post_graduate_year = models.CharField(max_length=4, blank=True, null=True)
    post_graduate_percent = models.CharField(max_length=10, blank=True, null=True)
    post_graduate_attach = models.FileField(upload_to='documents/', blank=True, null=True)
    
   
    uset = models.BooleanField(default=False)
    phd = models.BooleanField(default=False)
    work_experience = models.TextField(blank=True, null=True)
    internship = models.TextField(blank=True, null=True)
    seminars = models.TextField(blank=True, null=True)
    publications = models.TextField(blank=True, null=True)
    hobby = models.CharField(max_length=100, blank=True, null=True)
    sports = models.CharField(max_length=100, blank=True, null=True)
    
    reference = models.TextField(blank=True, null=True)
    other_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Vacancy Register"
        verbose_name_plural = "Vacancy Registers"
