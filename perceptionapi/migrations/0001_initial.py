# Generated by Django 3.1.2 on 2022-11-29 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countrylist', '0002_auto_20221125_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerceptionScore',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('easy_of_registration', models.FloatField(max_length=1)),
                ('compliance', models.FloatField(max_length=1)),
                ('tax', models.FloatField(max_length=1)),
                ('incentives', models.FloatField(max_length=1)),
                ('movements_of_financial_resources', models.FloatField(max_length=1)),
                ('support_for_civil_rights', models.FloatField(max_length=1)),
                ('country_of_focus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countrylist.countrylist')),
            ],
        ),
    ]