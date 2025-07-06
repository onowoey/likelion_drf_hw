from django.db import models

# Create your models here.
class Singer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    content = models.TextField()
    debut = models.DateField()
    
class Song(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    singer = models.ForeignKey(Singer, blank= False, null = False, on_delete=models.CASCADE, related_name='songs')
    content = models.TextField()
    release = models.DateField()