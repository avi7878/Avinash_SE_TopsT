from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    salary = models.IntegerField()
    photo = models.ImageField(upload_to='photo/',null=True,blank=True)

    class Meta:
        db_table = "user"
