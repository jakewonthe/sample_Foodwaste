from django.db import models

# Create your models here.


class Donar_Model(models.Model):

    fullname=models.CharField(max_length=40)

    email=models.CharField(max_length=40)

    fooditems=models.CharField(max_length=100)

    address=models.TextField(default="enter the address")

    phone=models.CharField(max_length=20)

    orphanage=models.CharField(max_length=30)

    date=models.DateField()

    def __str__(self):

        return self.fullname


class Agent_Model(models.Model):

    name=models.CharField(max_length=40)

    password=models.CharField(max_length=40)

    email=models.CharField(max_length=50)

    phone=models.CharField(max_length=20)

    address=models.TextField(default="Enter the address")

    
    def __str__(self):

        return self.name

class Assign_Model(models.Model):

    cid=models.IntegerField(primary_key=True)
    
    aid=models.IntegerField()

    def __str__(self):

       return self.cid
    

