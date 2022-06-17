from django.db import models

# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=16, unique=True)
    def __str__(self):      # чтобы в Админке выводилось по русски
        return self.name

class Tovar (models.Model):
    name = models.CharField(max_length=32, unique=True)
    price= models.IntegerField()
    # одна категория - много товаров:
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):      # чтобы в Админке выводилось по русски
        return self.name


