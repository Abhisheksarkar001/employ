from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth import settings

# Create your models here.
class Employ(models.Model):

    objects = models.Manager()
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)
    class Meta:
        """doc string here"""
        verbose_name_plural = "Employs"
        verbose_name = "Employ"

class EmployWorkReport(models.Model):

    objects = models.Manager()
    employ = models.ForeignKey(Employ, on_delete=models.CASCADE, null=True)
    date = models.DateField(default=datetime.now, null=True, blank=True) 
    total_classes_taken = models.IntegerField(default=0)
    total_video_record = models.IntegerField(default=0)
    work_ppt_topic = models.CharField(max_length=200)
    employ_task_detail_report = models.CharField(max_length=200)




    def __str__(self):
        return str(self.employ)
    class Meta:
        """doc string here"""
        verbose_name_plural = "EmpWorkReport"
        verbose_name = "EmpWorkReport"

class TeacherClassTaken(models.Model):

    objects = models.Manager()
    work = models.ForeignKey(EmployWorkReport, on_delete=models.CASCADE, null=True)
    course = models.CharField(max_length=200)
    semester = models.CharField()
    subject = models.CharField(max_length=100)
    STATUS_CHOICES = (
        (1, "Offline"),
        (2, "Online"),
    )
    class_mode = models.IntegerField(choices=STATUS_CHOICES, default=1)


    def __str__(self):
        return str(self.course)
    class Meta:
        """doc string here"""
        verbose_name_plural = "TeacherClassTaken"
        verbose_name = "TeacherClassTaken"


class TeacherVideoRecord(models.Model):

    object = models.Manager()
    work = models.ForeignKey(EmployWorkReport, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    duration = models.IntegerField()



    def __str__(self):
        return str(self.subject)
    class Meta:
        """doc string here"""
        verbose_name_plural = "TeacherVideoRecord"
        verbose_name = "TeacherVideoRecord"


class WorkPPTTopic(models.Model):

    objects = models.Manager()
    work = models.ForeignKey(EmployWorkReport, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.work)
    class Meta:
        """doc string here"""
        verbose_name_plural = "WorkPPTTopic"
        verbose_name = "WorkPPTTopic"



class EmployTeskDetailReport(models.Model):
    TASK_STATUS_CHOICES = [
        (1, 'In Process'),
        (2, 'Completed'),
        (3, 'Not Completed'),
       
    ]
    object = models.Manager()
    work = models.ForeignKey(EmployWorkReport, on_delete=models.CASCADE, null=True)
    task_name = models.CharField(max_length=255)
    employ_id = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    task_detail_attach = models.FileField(upload_to='document/', null=True, blank=True)
    assign_date = models.DateField(default=datetime.now, null=True, blank=True)
    completed_date = models.DateField(default=datetime.now, null=True, blank=True)
    actual_completed_date = models.DateField(default=datetime.now, null=True, blank=True)
    status = models.CharField(max_length=20, choices=TASK_STATUS_CHOICES, default=1)
    task_report_attach = models.FileField(upload_to='document/', null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        editable=False,
        null=True,
        blank=True,
    )
    approved_by = models.CharField(max_length=255)
    ranking = models.IntegerField()

    def __str__(self):
        return str(self.name)
    class Meta:
        """doc string here"""
        verbose_name_plural = "EmployTeskDetailReport"
        verbose_name = "EmployTeskDetailReport"



class EmployLeaveApplication(models.Model):
    LEAVE_STATUS_CHOICES = [
        (1, 'Pending'),
        (2, 'Approved'),
        (3, 'Rejected'),
    ]
    object = models.Manager()
    work = models.ForeignKey(EmployWorkReport, on_delete=models.CASCADE, null=True)
    employ_id = models.CharField(max_length=50)
    apply_date = models.DateField(default=datetime.now, null=True, blank=True)
    leave_from = models.DateField(default=datetime.now, null=True, blank=True)
    leave_to = models.DateField(default=datetime.now, null=True, blank=True)
    leave_reason = models.TextField(null=True, blank=True)
    leave_type = models.CharField(max_length=20,)
    attach_file = models.FileField(upload_to='documents/', null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        editable=False,
        null=True,
        blank=True,
    )
    leave_status = models.CharField(max_length=20, choices=LEAVE_STATUS_CHOICES, default=1)
    approved_by = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.employ_id)
    class Meta:
        """doc string here"""
        verbose_name_plural = "EmployLeaveApplication"
        verbose_name = "EmployLeaveApplication"

    


