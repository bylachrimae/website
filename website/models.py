from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150,default='Title')
    title_turkish = models.CharField(max_length=150,default='Turkish Title')
    description = models.TextField(blank=True)
    description_turkish = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
class Project(models.Model):
    title = models.CharField(max_length=250,default='Title')
    title_turkish = models.CharField(max_length=250,default='Turkish Title')
    project_content = models.TextField(blank=True)
    project_content_turkish = models.TextField(blank=True)
    image = models.ImageField(upload_to="uploads/", height_field=None, width_field=None, max_length=None,default=True)
    image2 = models.ImageField(upload_to="uploads/", height_field=None, width_field=None, max_length=None,null=True,blank=True)
    image3 = models.ImageField(upload_to="uploads/", height_field=None, width_field=None, max_length=None,null=True,blank=True)
    image4 = models.ImageField(upload_to="uploads/", height_field=None, width_field=None, max_length=None,null=True,blank=True)
    image5 = models.ImageField(upload_to="uploads/", height_field=None, width_field=None, max_length=None,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    programming_languages = models.CharField(max_length=255,default="SQL")
    project_link = models.CharField(max_length=255,null=True,blank=True)
    project_githublink = models.CharField(max_length=255,null=True,blank=True)
    project_playstorelink = models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self):
        return self.title
    

class MySkill(models.Model):
    title = models.CharField(max_length=50,default="Title")
    percentage = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.title
    
class Personal(models.Model):
    title = models.CharField(max_length=250,default='Title')
    image = models.ImageField(upload_to="uploads/",height_field=None, width_field=None, max_length=None)
    coverletter_turkish = models.TextField(blank=True)
    coverletter_english = models.TextField(blank=True)
    turkishCV = models.FileField(upload_to="uploads/cv")
    englishCV =models.FileField(upload_to="uploads/cv")
    linkedin_url = models.CharField(max_length=255,null=True)
    github_url = models.CharField(max_length=255,null=True)
    youtube_url = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.title