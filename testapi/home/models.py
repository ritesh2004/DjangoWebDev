from django.db import models

# Create your models here.
class Books(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    def __str__(self):
        return self.title