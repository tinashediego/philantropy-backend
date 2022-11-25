from django.db import models

# Create your models here.
class CountryList(models.Model):
    id = models.CharField(max_length=3, primary_key=True, null=False, blank=False)
    country_name = models.CharField(max_length=500)
    

    def __str__(self):
        return self.country_name
