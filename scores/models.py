from django.db import models

# Create your models here.
class Student(models.Model):
    # Registration number
    sbd = models.CharField(max_length=20, unique=True)

    # Subjects (nullable because not every student has all subjects)
    toan = models.FloatField(null=True, blank=True)
    ngu_van = models.FloatField(null=True, blank=True)
    ngoai_ngu = models.FloatField(null=True, blank=True)
    vat_li = models.FloatField(null=True, blank=True)
    hoa_hoc = models.FloatField(null=True, blank=True)
    sinh_hoc = models.FloatField(null=True, blank=True)
    lich_su = models.FloatField(null=True, blank=True)
    dia_li = models.FloatField(null=True, blank=True)
    gdcd = models.FloatField(null=True, blank=True)

    # This is like "English code" (e.g. N1)
    ma_ngoai_ngu = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.sbd
