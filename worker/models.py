from django.db import models

# Create your models here.

class Project(models.Model):
    NAME=models.CharField(max_length=20)
    DESC=models.CharField(max_length=200)
    TAGS=models.CharField(max_length=100)
    THUMBNAIL=models.URLField(max_length=500)
    URL=models.URLField(max_length=500)

    def __str__(self):
        return self.NAME

class Blog(models.Model):
    TITLE=models.CharField(max_length=100)
    DESC=models.CharField(max_length=200)
    TAGS=models.CharField(max_length=100)
    THUMBNAIL=models.URLField(max_length=500)
    URL=models.URLField(max_length=500)

    def __str__(self):
        return self.TITLE