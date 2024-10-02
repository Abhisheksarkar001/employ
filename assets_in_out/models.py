from django.db import models
from django.contrib.auth import settings
from django.utils.timezone import datetime


# Create your models here.
class AssetsInOut(models.Model):

    objects = models.Manager()
    assets_no = models.CharField(max_length=100,)
    name = models.CharField(max_length=255,)
    out_date =  models.DateField(default=datetime.now, null=True, blank=True, editable=False)
    reason = models.TextField(null=True, blank=True)
    in_date =  models.DateField(default=datetime.now, null=True, blank=True, editable=False)
    technician_mo_no = models.CharField(max_length=15)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    approved_by = models.CharField(max_length=100,)

    def __str__(self):
        return str(self.assets_no)

    class Meta:
        verbose_name_plural = "Assets In-Out Records"
        verbose_name = "Assets In-Out Record"
