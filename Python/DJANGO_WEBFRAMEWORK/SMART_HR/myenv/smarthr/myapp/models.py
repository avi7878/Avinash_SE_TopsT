from django.db import models

# Create your models here.

""""

                                User
                                  |
                                  v
                                email
                                password
                                role
                                  |
                                  v
        -------------------------------------------------
        |                                                |    
        v                                                v
        HR                                             employees


"""

class User(models.Model):
    email = models.EmailField(unique=True,max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30)

class Hr(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name  = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=30)

class Employees(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name  = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    birth_date = models.CharField(max_length=20)
    special_interests = models.CharField(max_length=30)
    education = models.CharField(max_length=30)
    marital_status = models.CharField(max_length=30)
