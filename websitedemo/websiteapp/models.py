from django.db import models

# Create your models here.

 


class aboutus(models.Model):
    heading=models.CharField(max_length=50,null=True)
    desc1=models.CharField(max_length=200,null=True)
    desc2=models.CharField(max_length=200,null=True)
    desc3=models.CharField(max_length=200,null=True)
    img=models.ImageField(upload_to="img/about",null=True)
    submitted_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:"aboutus"

    def __str__(self):
        return self.heading  


class clients(models.Model):
    heading=models.CharField(max_length=50,null=True)
    
    img=models.ImageField(upload_to="img/clients",null=True)
    submitted_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:"clients"


class features(models.Model):
    heading=models.CharField(max_length=50,null=True)
    desc=models.CharField(max_length=200,null=True)
    img=models.ImageField(upload_to="img/features",null=True)
    submitted_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:"features"


class carousel(models.Model):
    
    heading=models.CharField(max_length=50,null=True)
    desc=models.CharField(max_length=200,null=True)
    img=models.ImageField(upload_to="img/carousel",null=True)
    submitted_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:"carousel"


