
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location='pic/%y/')
from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    sname = models.CharField(max_length=150)
    tags = models.TextField()
    sdesc = models.TextField()
    ldesc = models.TextField()
    img = models.FileField(upload_to="pic/%y/")
    def __str__(self):
        return self.title
    class Meta:
        ordering=('id',)
    
    def get_absolute_url(self):
        return reverse('details',args=[self.id,self.slug])
    
class Notes(models.Model):
    plantname = models.CharField(max_length=100)  # Ensures the field is indented under the class
    description = models.TextField()
    image = models.FileField(upload_to='plant_images/')

    def __str__(self):
        return self.plantname
  