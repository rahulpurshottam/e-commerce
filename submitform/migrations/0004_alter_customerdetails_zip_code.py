# Generated by Django 5.1.4 on 2024-12-24 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submitform', '0003_customerdetails_delete_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetails',
            name='zip_code',
            field=models.CharField(max_length=10),
        ),
    ]
