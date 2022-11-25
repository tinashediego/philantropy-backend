# Generated by Django 3.1.2 on 2022-11-25 08:49

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('countrylist', '0001_initial'),
        ('sadcapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='ISO_A3',
        ),
        migrations.RemoveField(
            model_name='country',
            name='country_name',
        ),
        migrations.AddField(
            model_name='country',
            name='country',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='countrylist.countrylist'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='country',
            name='summaryStatement',
            field=tinymce.models.HTMLField(),
        ),
    ]