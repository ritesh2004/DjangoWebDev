from django.db import models

# Create your models here.

class quiz(models.Model):
    quizid = models.CharField(max_length=500)
    qn = models.CharField(max_length=1000)
    qnno = models.IntegerField(default=False)
    Op_a = models.CharField(max_length=1000)
    Op_b = models.CharField(max_length=1000)
    Op_c = models.CharField(max_length=1000)
    Op_d = models.CharField(max_length=1000)
    correct = models.CharField(max_length=1000)
    
    def  __str__(self):
        return self.quizid
    