from django.db import models

from countrylist.models import CountryList

# Create your models here.
class Reports(models.Model):
    id = models.AutoField(primary_key=True)
    country_of_focus = models.ForeignKey(CountryList, on_delete=models.CASCADE)
    report_files = models.FileField(upload_to = "law-files", blank=True)
    
    def __str__(self):
        return self.country_of_focus.country_name