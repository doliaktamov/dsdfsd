from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)


class Company(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=50)
    money_product = models.CharField(max_length=100)
    quantity_product = models.CharField(max_length=15)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

