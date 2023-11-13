from django.db import models

class State(models.Model):
    name = models.CharField(primary_key=True, max_length=50, null=False, blank=False, default="")
    valid_data = models.BooleanField(null=False, blank=False, default=False)
    population = models.IntegerField(null=False, default=0)
    obesity_percentage_afflicted = models.IntegerField(null=True, blank=True, default=0)
    obesity_population_afflicted = models.IntegerField(null=True, blank=True, default=0)
    diabetes_percentage_afflicted = models.IntegerField(null=True, blank=True, default=0)
    diabetes_population_afflicted = models.IntegerField(null=True, blank=True, default=0)
    mean_obesity_percentage = models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True, default=0)
    mean_diabetes_percentage = models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True, default=0)
    std_obesity_percentage = models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True, default=0)
    std_diabetes_percentage = models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True, default=0)

class County(models.Model):
    id = models.CharField(primary_key=True, max_length=55, null=False, blank=False, default="")
    state = models.CharField(max_length=50, null=False, blank=False, default="")
    county = models.CharField(max_length=50, null=False, blank=False, default="")
    valid_data = models.BooleanField(null=False, blank=False, default=False)
    population = models.IntegerField(null=False, default=0)
    obesity_percentage_afflicted = models.IntegerField(null=True, blank=True, default=0)
    obesity_population_afflicted = models.IntegerField(null=True, blank=True, default=0)
    diabetes_percentage_afflicted = models.IntegerField(null=True, blank=True, default=0)
    diabetes_population_afflicted = models.IntegerField(null=True, blank=True, default=0)
