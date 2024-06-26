# Generated by Django 4.2.7 on 2024-01-05 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_order_address_order_full_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'Товар в кошику', 'verbose_name_plural': 'Товари в кошику'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Замовлення', 'verbose_name_plural': 'Замовлення'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Товар в замовленні', 'verbose_name_plural': 'Товари в замовленні'},
        ),
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default='a', upload_to='img/'),
            preserve_default=False,
        ),
    ]
