from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

from django.db import models


class System(models.Model):
    serialNumberInserv = models.CharField(primary_key=True, max_length = 20)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.serialNumberInserv
"""
class Tenant(models.Model):
    TenantID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=20)
    systemIDs = ArrayField(models.ForeignKey(System, on_delete = models.CASCADE), size = 128,)

class User(models.Model):
    UserID = models.IntegerField(primary_key=True)
    UserName = models.CharField(max_length=20)
    PasswordKey= models.CharField(max_length=32)
    TenantID = models.ForeignKey(Tenant, on_delete = models.CASCADE)
"""

class File(models.Model):
    FileID = models.CharField(primary_key=True, max_length = 30)
    name = models.CharField(max_length=20)
    filePath = models.CharField(max_length=100)
    dataDate = models.DateField()
    SystemID = models.ForeignKey(System, on_delete = models.CASCADE)

    def __str__(self):
        return self.FileID
