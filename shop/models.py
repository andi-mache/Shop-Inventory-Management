from django.db import models


class Categories(models.Model):
    category_id = models.CharField(max_length=20)
    cat_name = models.CharField(max_length=100 ,unique=True)
    class Meta:
        db_table = "categories"


class Item(models.Model):
    cat_gar = models.ForeignKey(Categories, on_delete=models.CASCADE)
    category_name = models.OneToOneField(Categories, related_name="item_cat_name",to_field="cat_name",on_delete=models.CASCADE )
    item_name = models.CharField(max_length=100)
    price_per_unit = models.IntegerField()
    quantity = models.CharField(max_length=100)

    class Meta:
        db_table = "shop_item"

class CatSales(models.Model):
    cat_sales = models.ForeignKey(Categories, on_delete=models.CASCADE)
    catgars_name = models.OneToOneField(Item, related_name="profit_cat_name",to_field="category_name",on_delete=models.CASCADE ,default="category name")
    year = models.IntegerField()
    month = models.CharField(max_length=100)
    sales = models.IntegerField()
    profit = models.IntegerField()
    class Meta:
        db_table = "profit_sales"

