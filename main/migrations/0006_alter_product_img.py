# Generated by Django 4.2.7 on 2024-01-05 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_cartitem_options_alter_order_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.CharField(max_length=100, verbose_name='Посилання на зображення'),
        ),
    ]
