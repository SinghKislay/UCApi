# Generated by Django 2.1.5 on 2019-03-11 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20190227_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='location',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]