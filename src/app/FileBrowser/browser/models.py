from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

from django.db import models


class System(models.Model):
    serialNumberInserv = models.CharField(primary_key=True, max_length = 45)
    name = models.CharField(max_length=45)
    def __str__(self):
        return self.serialNumberInserv

class customUser(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20)

class File(models.Model):
    FileID = models.CharField(primary_key=True, max_length = 45)
    name = models.CharField(max_length=35)
    filePath = models.CharField(max_length=100)
    dataDate = models.DateField()
    SystemID = models.ForeignKey(System, on_delete = models.CASCADE)

    def __str__(self):
        return self.FileID
