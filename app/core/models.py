from django.db import models

# Create your models here.
class Sample(models.Model):
    name=models.CharField(max_length=24,default='user')

    def __str__(self):
        return self.name