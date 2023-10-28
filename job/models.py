from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone
from django.utils.text import slugify
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
    slug=models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Job,self).save(*args,**kwargs)

class Category(models.Model):
    name=models.CharField(max_length=40)
    logo=models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.name

class Company(models.Model):
     name=models.CharField(max_length=50)
     logo=models.ImageField(upload_to='company')
     subtitle=models.TextField(max_length=1000)
     website=models.URLField()
     email=models.EmailField()
     def __str__(self):
        return self.name
    