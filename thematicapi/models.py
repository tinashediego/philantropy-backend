from django.db import models
from countrylist.models import CountryList
# Create your models here.
class ThematicArea(models.Model):
    id = models.AutoField(primary_key=True)
    country_of_focus = models.ForeignKey(CountryList, on_delete=models.CASCADE)
    easy_of_registration = models.FloatField(max_length=1, blank=False)
    compliance = models.FloatField(max_length=1, blank=False)
    tax = models.FloatField(max_length=1, blank=False)
    incentives = models.FloatField(max_length=1, blank=False)
    movements_of_financial_resources = models.FloatField(max_length=1, blank=False)
    support_for_civil_rights = models.FloatField(max_length=1, blank=False)

    def __str__(self):
        return self.country_of_focus.country_name