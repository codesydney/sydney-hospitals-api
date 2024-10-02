from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    suburb = models.CharField(max_length=255)
    postcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email_address = models.EmailField()
    fax = models.CharField(max_length=20)
    lhd = models.CharField(max_length=100)
    hospital_website = models.URLField()
    ed = models.CharField(max_length=20)

    class Meta:
        db_table = 'nsw_hospitals_table'
        managed = False  # Set to False to use the existing table
