from django.db import models
from tinymce import models as tinymce_models
from countrylist.models import CountryList

# Create your models here.
class Law(models.Model):
    id = models.AutoField(primary_key=True)
    targeted_country = models.ForeignKey(CountryList, on_delete=models.CASCADE)
    law = tinymce_models.HTMLField()
    law_description = tinymce_models.HTMLField()
    source_name = models.TextField(blank=True, default='')
    source_link = models.CharField(max_length=500, blank=True, default='')

    def __str__(self):
        return self.targeted_country.country_name
