# signup/models.py
from django.db import models
# from django.contrib.auth.models import User

class UserProfile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    state = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    account = models.CharField(max_length=20)
    # debitcard = models.BooleanField(default=False)
    # creditcard = models.BooleanField(default=False)
    # checkbook = models.BooleanField(default=False)
    materials=models.CharField(max_length=20,default="credit card")


    def __str__(self):
        return self.name

