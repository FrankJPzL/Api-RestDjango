from django.db import models

# Create your models here.
class Company(models.Model):
    usuarioname = models.CharField(max_length=50)
    nombreapellido = models.CharField(max_length=100)
    nombreapellido_2 = models.CharField(max_length=100)


class Usuario(models.Model):
    Usuario = models.CharField(max_length=100)






