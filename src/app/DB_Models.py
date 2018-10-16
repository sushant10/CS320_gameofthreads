from django.db import models

class User(models.Model):
    UserID = models.IntegerField(primary_key=True)
    UserName = models.CharField(max_length=20)
    PasswordKey= models.CharField(max_length=32)
    TenantID = models.ForeignKey(Tenant)

class Tenant(models.Model):
    TenantID = model.IntegerField(primary_key=True)
    Name = models.CharField(max_length=20)
    systemIDs = ArrayField(models.ForeignKey(System), size = 128)

class System(models.Model):
    serialNumberInserv = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

class File(models.Model):
    FileID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    filePath = models.CharField(max_length=40)
    dataDate = models.DateField()
    SystemID = models.ForeignKey(System)
