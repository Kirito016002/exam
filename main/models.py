from django.db import models

class Contact(models.Model):
    fullname = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    email = models.EmailField()
    massage = models.TextField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.fullname
    
    class Meta():
        verbose_name = "Xabar"
        verbose_name_plural = "Xabarlar" 
        
        
class Service(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    icon_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name = "Xizmat"
        verbose_name_plural = "Xizmatlar" 
        
        
class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='blog_image/')
    
    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name = "Ma`lumot"
        verbose_name_plural = "Kompaniya haqida ma`lumot" 
        
        
class Sponsour(models.Model):
    image = models.ImageField(upload_to='sponsour_icon/')
    
    
    class Meta():
        verbose_name = "Sponsor"
        verbose_name_plural = "Sponsorlar" 
        
        
class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio/')
    
    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar" 
        
        
class Team(models.Model):
    fullname = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="team/")
    
    def __str__(self):
        return self.fullname
    
    class Meta():
        verbose_name = "Jamoa a`zosi"
        verbose_name_plural = "Jamoa" 