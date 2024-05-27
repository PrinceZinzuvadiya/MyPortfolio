from django.db import models

class contactmodel(models.Model):
    inserted=models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    message = models.TextField()
