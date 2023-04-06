from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from django.db.models.base import Model


class Jobs(models.Model):
    job_id = models.AutoField
    job_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    salary = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    application_date = models.DateField()

    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.job_name


class UpdateProfile(models.Model):
    username = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    mobile = models.CharField(max_length=50, default="")
    address1 = models.CharField(max_length=50, default="")
    address2 = models.CharField(max_length=50, default="")
    bio = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Resume(models.Model):
    username = models.CharField(max_length=50, default="")
    fullname = models.CharField(max_length=50, default="")
    fathername = models.CharField(max_length=50, default="")
    mothername = models.CharField(max_length=50, default="")
    ssc = models.CharField(max_length=50, default="")
    inter = models.CharField(max_length=50, default="")
    degree = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Blog(models.Model):
    username = models.CharField(max_length=50, default="")
    title = models.CharField(max_length=50, default="")
    blog = models.CharField(max_length=50, default="")
    date = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.username


class Apply(models.Model):
    username = models.CharField(max_length=50, default="")
    date = models.CharField(max_length=50, default="")
    email = models.EmailField()
    work = models.CharField(max_length=50, default="")
    experience = models.CharField(max_length=50, default="", null=False)
    graduation_date = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.username


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    num = models.CharField(max_length=12)
    desc = models.TextField(max_length=250)

    def __str__(self):
        return self.name
