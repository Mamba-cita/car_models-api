from django.db import models

# Create your models here.

class Vox(models.Model):
    name = models.CharField(max_length=50)
    model=models.CharField(max_length=10)
    company=models.CharField(max_length=50)
    email=models.EmailField(max_length=50, unique=True)
    country=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    