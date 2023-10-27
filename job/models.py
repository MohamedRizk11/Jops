from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone
# Create your models here.


job_type=(
    ('fulltime','fulltime'),
    ('parttime','parttime'),
    ('remote','remote'),
    ('freelance','freelance'),



)
class Job(models.Model):
    title = models.CharField(max_length=120)
    loction = CountryField()
    company=models.ForeignKey('Company',on_delete=models.CASCADE,related_name='jop_company')
    create_at =models.DateTimeField(default=timezone.now)
    salary_start=models.IntegerField(null=True,blank=True)
    salary_end=models.IntegerField(null=True,blank=True)
    description=models.TextField(max_length=15000)
    vecancy=models.IntegerField()
    job_nature=models.CharField(choices=job_type,max_length=10)
    experience=models.IntegerField()
    category=models.ForeignKey('Category',on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.title

class Category(models.Model):
    name=models.CharField(max_length=40)
    logo=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Company(models.Model):
     name=models.CharField(max_length=50)
     logo=models.ImageField('company')
     subtitle=models.TextField(max_length=1000)
     website=models.URLField()
     email=models.EmailField()
     def __str__(self):
        return self.name
    