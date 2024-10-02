from django.db import models
from django.utils.timezone import datetime


# Create your models here.

class PlacementRegister(models.Model):
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
        ('Placed', 'Placed'),
        ('In Process', 'In Process'),
        ('Not Eligible', 'Not Eligible'),
    ]
    
    LEVEL_CHOICES = [
        ('School', 'School'),
        ('College', 'College'),
        ('University', 'University'),
        ('District', 'District'),
        ('State', 'State'),
        ('National', 'National'),
        ('International', 'International'),
    ]
    
    RANK_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('Participated', 'Participated'),
    ]
    
    objects =  models.Manager()
    student_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    mo_no = models.CharField(max_length=15)
    mail_id = models.EmailField(max_length=100)
    aadhaar_no = models.CharField(max_length=12)
    pan_no = models.CharField(max_length=10, blank=True, null=True)
    father_name = models.CharField(max_length=100)
    father_mo_no = models.CharField(max_length=15, blank=True, null=True)
    father_mail_id = models.EmailField(max_length=100, blank=True, null=True)
    mother_name = models.CharField(max_length=100)
    mother_mo_no = models.CharField(max_length=15, blank=True, null=True)
    sex = models.CharField(max_length=10)
    dob = models.DateField(default=datetime.now, null=True, blank=True, editable=False)
    religion = models.CharField(max_length=50, choices=RELIGION_CHOICES)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    address = models.TextField()
    city_district = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
    
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    placed_organization_name = models.CharField(max_length=100, blank=True, null=True)
    salary_per_annum = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    placement_date =  models.DateField(default=datetime.now, null=True, blank=True, editable=False)
    biodata_attach = models.FileField(upload_to='document/', blank=True, null=True)
    offer_letter_attach = models.FileField(upload_to='document/', blank=True, null=True)
    
    
    roll_no = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50)
    board_university_name = models.CharField(max_length=100)
    school_college_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    year = models.IntegerField(default=0)
    percent_grade = models.DecimalField(max_digits=5, decimal_places=2)
    
    
    company_organization = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    no_of_year_service = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    work_profile = models.TextField(blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
   
    internship_company_organization = models.CharField(max_length=100, blank=True, null=True)
    internship_designation = models.CharField(max_length=100, blank=True, null=True)
    internship_no_of_year_service = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    internship_work_profile = models.TextField(blank=True, null=True)
    
   
    seminar_title = models.CharField(max_length=100, blank=True, null=True)
    seminar_date = models.DateField(default=datetime.now, null=True, blank=True, editable=False)
    seminar_presented_in = models.CharField(max_length=100, blank=True, null=True)
    seminar_published = models.BooleanField(default=False)
    seminar_attach = models.FileField(upload_to='seminars/', blank=True, null=True)
    
 
    publication_book_name = models.CharField(max_length=100, blank=True, null=True)
    publication_issn_no = models.CharField(max_length=50, blank=True, null=True)
    publication_publisher = models.CharField(max_length=100, blank=True, null=True)
    publication_attach = models.FileField(upload_to='document/', blank=True, null=True)
    
    
    sport_name = models.CharField(max_length=100, blank=True, null=True)
    sport_level = models.CharField(max_length=50, choices=LEVEL_CHOICES, blank=True, null=True)
    sport_date = models.DateField(blank=True, null=True)
    sport_rank = models.CharField(max_length=50, choices=RANK_CHOICES, blank=True, null=True)
    sport_attach = models.FileField(upload_to='document/', blank=True, null=True)

    def __str__(self):
        return str(self.student_id)

    class Meta:
        verbose_name = "Placement Register"
        verbose_name_plural = "Placement Registers"
