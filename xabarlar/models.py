from django.db import models

# Create your models here.
class Maqola(models.Model):
    sarlavha = models.CharField(max_length=100)
    matn = models.TextField(max_length=500)
    def __str__(self):
        return self.sarlavha