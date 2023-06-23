from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Purchase(models.Model):
    name = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class PurchasedProduct(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    

    def __str__(self):
        return f'{self.purchase.name} - {self.product.name}'