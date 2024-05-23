# Generated by Django 4.2.7 on 2023-12-27 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='full_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]