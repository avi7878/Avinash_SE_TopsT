from django.db import models

# Create your models here.
"""
                                    User
                                      |
                                      v
                                    email
                                    password
                                    role
                                      |
                                      v
                ----------------------------------------
                |                                      |
                v                                      v
             chairman                           Society Member            
"""

class User(models.Model):
    email = models.EmailField(unique=True,max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30)

    def __str__(self):
        return self.email    

class Chairman(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contactno = models.CharField(max_length=30)
    pic = models.FileField(upload_to="media/images",default="media/dafault.webp")

    def __str__(self):
        return self.firstname

class SocietyMember(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contactno = models.CharField(max_length=30)
    no_of_familymember = models.CharField(max_length=30)
    house_no = models.CharField(max_length=10)
    vehical_details = models.CharField(max_length=30)
    no_of_vehicle = models.CharField(max_length=10)
    occupation = models.CharField(max_length=30)
    job_address = models.CharField(max_length=100,blank=True,null=True)
    pic = models.FileField(upload_to="media/images",default="media/dafault.webp")
    
    

