from django.db import models
from Todobackend.settings import BASE_DIR


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return str(BASE_DIR)+'/listtodo/static/img/{}'.format(filename)

class Todoapp(models.Model):
    id =models.AutoField(primary_key =True)
    title  = models.CharField(max_length=30)
    desc = models.CharField(max_length=60)
    active = models.CharField(max_length=5)
    def __str__(self):
        return self.title

class Todoapps(models.Model):
    id =models.AutoField(primary_key =True)
    title  = models.CharField(max_length=30)
    desc = models.CharField(max_length=60)
    active = models.CharField(max_length=5)
    file_pic = models.ImageField(upload_to='listtodo/static/img' )
    def __str__(self):
        return self.title

class Cricketapp(models.Model):
    id =models.AutoField(primary_key =True)
    title  = models.CharField(max_length=30)
    opposition = models.CharField(max_length=60)
    venue = models.CharField(max_length=5)
    def __str__(self):
        return self.title

class Cricket(models.Model):
    id =models.AutoField(primary_key =True)
    title  = models.CharField(max_length=30)
    opposition = models.CharField(max_length=60)
    venue = models.CharField(max_length=5)
    file_pic = models.ImageField(upload_to='listtodo/static/img' )
    def __str__(self):
        return self.title


























# Create your models here.
