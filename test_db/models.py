from django.db import models

# Create your models here.
class Document(models.Model):
    file_path = models.FileField(upload_to='files/%Y%m%d/')
    file_name = models.CharField(max_length=200)