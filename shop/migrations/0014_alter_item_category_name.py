# Generated by Django 4.0.1 on 2024-06-01 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_item_category_name_alter_item_cat_gar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='item_cat_name', to='shop.categories', to_field='cat_name'),
        ),
    ]
