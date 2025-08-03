from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    inventory = models.PositiveIntegerField()
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title
