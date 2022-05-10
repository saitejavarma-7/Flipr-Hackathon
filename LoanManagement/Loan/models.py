from django.db import models

# Create your models here.
class Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField( max_length=250)
    aadhar = models.FileField(upload_to='media')
    pancard = models.FileField(upload_to='media')
    salary = models.FileField(upload_to='media')
    photo = models.FileField(upload_to='media')
    bank = models.TextField()
    ctc = models.IntegerField()
    loan = models.IntegerField()
    def __str__(self):
        return self.name

class Request(models.Model):
    id = models.IntegerField(primary_key=True)
    loan_amt = models.IntegerField()
    acc_rej = models.BooleanField()
    tenure = models.IntegerField()
    interest = models.FloatField()
    

