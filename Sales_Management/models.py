from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return f"{self.username}"
    
class CategoryModel(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.name}'
    
class SaleModel(models.Model):
    product_name = models.CharField(max_length=255, null=True)
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='cat'
    )
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity = models.PositiveIntegerField(null=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True)
    tax_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    sale_date = models.DateField(auto_now_add=True)
      
    def __str__(self):
        return f"{self.product_name}---{self.unit_price}"
    
