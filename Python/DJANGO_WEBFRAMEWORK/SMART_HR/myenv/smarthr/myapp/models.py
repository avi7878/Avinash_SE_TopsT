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

    def __str__(self):
        return self.email

class Hr(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name  = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    pic = models.FileField(upload_to="media/images",default="media/default.webp")
    department = models.CharField(max_length=30,null=True)
    designation = models.CharField(max_length=30,null=True)
    date_of_join = models.TextField(max_length=50,null=True)
    email = models.EmailField(max_length=30,null=True)
    date_of_birth = models.TextField(max_length=50,null=True)
    # converted_date = models.TextField(max_length=50,null=True)
    address = models.TextField(max_length=50,null=True)
    gender = models.CharField(max_length=10,null=True)
    nationality = models.CharField(max_length=30,null=True)
    religion = models.CharField(max_length=30,null=True)
    marital_status = models.CharField(max_length=30,null=True)
    no_of_children = models.TextField(max_length=20,null=True)
    emergency_contact_name = models.CharField(max_length=20,null=True)
    relationship = models.CharField(max_length=20,null=True)
    emergency_contact_no = models.TextField(max_length=20,null=True)
    bank_name = models.CharField(max_length=30,null=True)
    bank_account_no = models.TextField(max_length=20,null=True)
    state = models.CharField(max_length=30,null=True)
    country = models.CharField(max_length=30,null=True)
    pin_code = models.CharField(max_length=30,null=True)
    family_member_name = models.CharField(max_length=20,null=True)
    family_member_relationship = models.CharField(max_length=20,null=True)
    family_member_birth_date = models.CharField(max_length=20,null=True)
    family_member_phone_no = models.TextField(max_length=20,null=True)
    institut_name = models.CharField(max_length=30,null=True)
    subject = models.CharField(max_length=30,null=True)
    institut_start_date = models.TextField(max_length=30,null=True)
    institut_complate_date = models.TextField(max_length=30,null=True)
    institut_degree_name = models.CharField(max_length=30,null=True)
    institut_degree_grade = models.CharField(max_length=30,null=True)


    def __str__(self):
        return self.first_name

class Employees(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name  = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=30)
    address = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=30,null=True)
    birth_date = models.CharField(max_length=20)
    special_interests = models.CharField(max_length=30)
    education = models.CharField(max_length=30)
    pic = models.FileField(upload_to="media/images",default="media/default.webp")
    department = models.CharField(max_length=30,null=True)
    gender = models.CharField(max_length=10,null=True)
    age = models.IntegerField(null=True)
    date_of_join = models.TextField(max_length=50,null=True)
    nationality = models.CharField(max_length=30,null=True)
    religion = models.CharField(max_length=30,null=True)
    marital_status = models.CharField(max_length=30,null=True)
    no_of_children = models.TextField(max_length=5,null=True)
    emergency_contact_name = models.CharField(max_length=20,null=True)
    relationship = models.CharField(max_length=20,null=True)
    emergency_contact_no = models.TextField(max_length=20,null=True)
    bank_name = models.CharField(max_length=30,null=True)
    bank_account_no = models.TextField(max_length=20,null=True)
    state = models.CharField(max_length=30,null=True)
    country = models.CharField(max_length=30,null=True)
    pin_code = models.CharField(max_length=30,null=True)
    family_member_name = models.CharField(max_length=20,null=True)
    family_member_relationship = models.CharField(max_length=20,null=True)
    family_member_birth_date = models.CharField(max_length=20,null=True)
    family_member_phone_no = models.TextField(max_length=20,null=True)
    institut_name = models.CharField(max_length=30,null=True)
    subject = models.CharField(max_length=30,null=True)
    institut_start_date = models.TextField(max_length=30,null=True)
    institut_complate_date = models.TextField(max_length=30,null=True)
    institut_degree_name = models.CharField(max_length=30,null=True)
    institut_degree_grade = models.CharField(max_length=30,null=True)


