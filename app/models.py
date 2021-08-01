from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class ProductModel(models.Model):
    product_name = models.CharField(max_length=100)
    product_model_name = models.CharField(max_length=100)
    price = models.IntegerField()
    categorymodel = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
