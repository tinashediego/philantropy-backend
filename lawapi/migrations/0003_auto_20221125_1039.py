# Generated by Django 3.1.2 on 2022-11-25 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countrylist', '0001_initial'),
        ('lawapi', '0002_auto_20221125_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='law',
            name='targeted_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countrylist.countrylist'),
        ),
    ]
