from django.db import models

# Create your models here.

"""
                                    user
                                      |
                                      v

                                    email
                                    password
                                    role
                                      |
                                      v
                 ------------------------------------------
                 |                                        |              
                 v                                        v
             chairman                               society member     
"""

class User(models.Model):
    email = models.EmailField(unique=True,max_length=50)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=20)
    otp = models.IntegerField(default=456)

    def __str__(self):
        return self.email
    
class Chairman(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=30)
    pic = models.FileField(upload_to="media/images",default="media/default.webp")

    def __str__(self):
        return self.first_name

class SocietyMember(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=30)
    no_of_family_member = models.CharField(max_length=30)
    house_no = models.CharField(max_length=30)
    vahical_details = models.CharField(max_length=10)
    vahical_no = models.CharField(max_length=30)
    occupation = models.CharField(max_length=30)
    job_address = models.CharField(max_length=30,blank=True,null=True)
    pic = models.FileField(upload_to="media/images",default="media/default.webp")

class Notice(models.Model):
    notice_title = models.CharField(max_length=50)
    notice_description = models.FileField()
    pic = models.FileField(upload_to="media/image",blank=True,null=True)
    video = models.FileField(upload_to="media/image",blank=True,null=True)
  
