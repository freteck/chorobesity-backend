# Generated by Django 4.2.5 on 2023-11-11 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chorobesity', '0005_rename_state_state_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='id',
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(default='', max_length=20, primary_key=True, serialize=False),
        ),
    ]