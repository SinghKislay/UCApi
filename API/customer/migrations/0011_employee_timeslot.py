# Generated by Django 2.1.5 on 2019-03-21 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_employee_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='timeslot',
            field=models.CharField(default='', max_length=50),
        ),
    ]
