# Generated by Django 5.1.4 on 2024-12-24 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submitform', '0004_alter_customerdetails_zip_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerdetails',
            name='discount',
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='country',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='cvv',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='payment_method',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]
