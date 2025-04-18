# Generated by Django 5.1.4 on 2024-12-22 12:14

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_product_desc_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_rev', models.CharField(max_length=100)),
                ('stars', models.CharField(max_length=10)),
                ('product_rate', models.FloatField(max_length=10)),
                ('review_des', tinymce.models.HTMLField()),
                ('product_image', models.ImageField(upload_to='product_images/')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='product_desc',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.FloatField(max_length=10),
        ),
    ]
