# Generated by Django 3.1.2 on 2022-11-29 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countrylist', '0002_auto_20221125_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('report_files', models.FileField(blank=True, upload_to='law-files')),
                ('country_of_focus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countrylist.countrylist')),
            ],
        ),
    ]