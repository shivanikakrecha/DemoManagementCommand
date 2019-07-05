from django.db import models

# Create your models here.
class ApiUsers(models.Model):
    name = models.CharField(max_length=20, verbose_name="name")
    username = models.CharField(max_length=20, verbose_name="username")
    email = models.EmailField(unique=True)
    website = models.CharField(max_length=20, verbose_name="name")

    def __str__(self):
        return self.name