from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Users(models.Model):
  
class File(models.Model):
    class file_type(models.TextChoices):
        DOCUMENT = 'doc', 'Document'
        IMAGE = 'img', 'Image'
        VIDEO = 'vid', 'Video'
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to="uploads/")
    file_type = models.CharField(max_length=3,
    choices=file_type.choices,
    default=file_type.DOCUMENT)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.filename