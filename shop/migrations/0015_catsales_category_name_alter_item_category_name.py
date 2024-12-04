# Generated by Django 4.0.1 on 2024-06-04 12:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_item_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='catsales',
            name='category_name',
            field=models.OneToOneField(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='profit_cat_name', to='shop.categories', to_field='cat_name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='category_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='item_cat_name', to='shop.categories', to_field='cat_name'),
        ),
    ]
