from django.db import models

class County(models.Model):
    # In this example, I'll use UUIDs for primary keys
    name = models.CharField(primary_key=True, max_length=20, null=False, blank=False)
    state = models.CharField(max_length=2, default="NA")
    type = models.CharField(max_length=20, default="")
    population = models.IntegerField(null=False, default=0)
    obesity_percentage_afflicted = models.IntegerField(null=True, blank=True, default=0)
    obesity_population_afflicted = models.IntegerField(null=True, blank=True, default=0)
    diabetes_percentage_afflicted = models.IntegerField(null=True, blank=True, default=0)
    diabetes_population_afflicted = models.IntegerField(null=True, blank=True, default=0)