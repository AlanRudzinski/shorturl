# Generated by Django 2.1.2 on 2018-11-11 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshort', '0003_auto_20181111_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorting',
            name='code',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='shorting',
            name='url_in',
            field=models.URLField(),
        ),
    ]
