# Generated by Django 3.2.24 on 2024-02-29 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_has_flower_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowercount',
            name='name',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]