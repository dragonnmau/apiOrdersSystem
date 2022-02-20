from operator import mod
from django.db import models

# Create your models here.
# crear migracion python manage.py makemigrations
# hacer migracion python manage.py migrate

class order(models.Model):
    nameOrder=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    todo=models.TextField(max_length=1000)
    status=models.PositiveSmallIntegerField(max_length=1) # 0 cancelada, 1 pendiente, 2 ejecucion, 3 finalizada
    docFile=models.CharField(max_length=200)
    crataedBy=models.IntegerField(max_length=11)
    assignTo=models.IntegerField(max_length=11)

class user(models.Model):
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    telephone = models.CharField(max_length=100)

class client(models.Model):
    company=models.CharField(max_length=25)
    phoneContact=models.PositiveIntegerField(max_length=25)
    nameContact=models.CharField(max_length=100)
    adressCom=models.CharField(max_length=25)
    