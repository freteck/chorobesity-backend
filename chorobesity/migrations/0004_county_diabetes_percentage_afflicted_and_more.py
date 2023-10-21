# Generated by Django 4.2.5 on 2023-10-21 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chorobesity', '0003_rename_id_county_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='county',
            name='diabetes_percentage_afflicted',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='county',
            name='diabetes_population_afflicted',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]