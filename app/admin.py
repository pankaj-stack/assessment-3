from app.models import CategoryModel, ProductModel
from django.contrib import admin
from .models import CategoryModel,ProductModel

# Register your models here.
admin.site.register(CategoryModel)
admin.site.register(ProductModel)