from django.db import models
from tinymce import models as tinymce_models
from lawapi.models import Law
from countrylist.models import CountryList
from thematicapi.models import ThematicArea

# Create your models here.

class CountryData(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.ForeignKey(CountryList, on_delete=models.CASCADE)
    thematic_area = models.ForeignKey(ThematicArea, on_delete=models.CASCADE)    
    flag = models.ImageField(upload_to = "images")
    summaryStatement = tinymce_models.HTMLField()
    otherLaws = models.ManyToManyField(Law, blank=True)

    def __str__(self):
        return self.country.country_name

