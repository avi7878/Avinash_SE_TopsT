from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.product_id}: {self.product_name}"
