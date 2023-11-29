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
    email = models.EmailField(unique=True,max_length=50,null=True)
    city = models.CharField(max_length=30,blank=True,null=True)
    blood_group = models.CharField(max_length=30)
    no_of_family_member = models.CharField(max_length=30)
    house_no = models.CharField(max_length=30)
    vahical_details = models.CharField(max_length=10)
    occupation = models.CharField(max_length=30)
    job_address = models.CharField(max_length=30,blank=True,null=True)
    pic = models.FileField(upload_to="media/images",default="media/default.webp")
    date_of_birth = models.TextField(max_length=30,blank=True,null=True)

    def __str__(self):
        return self.first_name

class Notice(models.Model):
    notice_title = models.CharField(max_length=50)
    notice_description = models.FileField()
    pic = models.FileField(upload_to="media/image",blank=True,null=True)
    video = models.FileField(upload_to="media/image",blank=True,null=True)
  
class Registration(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=30,blank=True,null=True)
    email = models.CharField(max_length=30,blank=True,null=True)
    password = models.CharField(max_length=10,blank=True,null=True)
    gender = models.CharField(max_length=30,blank=True,null=True)
    subject = models.CharField(max_length=20,blank=True,null=True)
    city = models.CharField(max_length=20,blank=True,null=True)
    contact_no = models.CharField(max_length=30,blank=True,null=True)    

    def __str__(self):
        return self.name
    
class event(models.Model):
    event_title = models.CharField(max_length=50)
    event_description = models.FileField()

class complaints(models.Model):
    complaints_description = models.FileField()

class maintainance(models.Model):
    title = models.CharField(max_length=50)
    amount = models.IntegerField(max_length=50)
    duedate = models.TextField(max_length=50)
