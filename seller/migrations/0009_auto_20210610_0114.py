# Generated by Django 3.2.3 on 2021-06-09 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0008_auto_20210610_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.ImageField(upload_to='product/'),
        ),
        migrations.AlterField(
            model_name='seller_shop_details',
            name='main_img',
            field=models.ImageField(upload_to='seller/'),
        ),
    ]
