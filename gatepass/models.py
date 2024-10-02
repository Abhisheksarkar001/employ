from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.
class GatePass(models.Model):
    PASS_TYPE_CHOICES = [
        ('Medical Emergency', 'Medical Emergency'),
        ('Personal Work', 'Personal Work'),
    ]
    
    APPROVAL_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    student_id = models.CharField(max_length=50)
    student_mo_no = models.CharField(max_length=15)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    pass_type = models.CharField(max_length=50, choices=PASS_TYPE_CHOICES)
    gate_pass_reason = models.TextField()
    parent_approval = models.CharField(max_length=3, choices=APPROVAL_CHOICES)
    approved_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='gatepass_approver'
    )
    
    def __str__(self):
        return str(self.student_id)
    class Meta:
        verbose_name = "Gate Pass"
        verbose_name_plural = "Gate Passes"
