# Generated by Django 2.1.4 on 2018-12-26 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientreport', '0002_auto_20181226_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdetails',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]