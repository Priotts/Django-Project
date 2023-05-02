from django.db import models
from django.contrib.auth.models import User
from .utils import SendTransaction
import json
from datetime import date
import hashlib

# Create your models here.yy
class Certificates(models.Model):
    code = models.CharField(max_length=5, unique=True) #unique code
    name_certificate = models.CharField(max_length=50, unique=True)
    note = models.CharField(max_length=200)
    def __str__(self):
        return self.name_certificate + ',' + self.code

    
class SetCertificates(models.Model):
    students = models.ForeignKey(User, on_delete=models.CASCADE)
    certificates = models.ForeignKey(Certificates, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    vote = models.PositiveIntegerField()
    hash = models.CharField(max_length=255, blank=True, null=True)
    txid = models.CharField(max_length=255, blank=True, null=True) 
    
    def write(self):
        data = {
            'code' : self.certificates.code,
            'first_name' : self.students.first_name,
            'last_name' : self.students.last_name,
            'certificate' : self.certificates.name_certificate,
            'note' : self.certificates.note,
            'vote' : self.vote,
            'date' : str(self.date)
        }

        data_json = json.dumps(data)
        
        print(data, 'json:', data_json)
        return SendTransaction(data_json)

    def save(self):
        self.txid = self.write()
        super (SetCertificates, self).save()

    def __str__(self) :
        return self.certificates.name_certificate
