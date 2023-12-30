from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser): #implements new field in the user table
    bio = models.TextField(max_length=500, blank=True)
    telephone = models.CharField(max_length=30, blank=True)
    
    USER_TYPES = [
        ('aluno', 'Aluno'),
        ('explicador', 'Explicador'), 
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default = '')

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    year = models.CharField(max_length=2, choices=[
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
], default='')
    
    school = models.TextField(max_length=100, blank=True)

    distritos_dict = {
        'Aveiro': 'Aveiro',
        'Beja': 'Beja',
        'Braga': 'Braga',
        'Bragança': 'Bragança',
        'Castelo Branco': 'Castelo Branco',
        'Coimbra': 'Coimbra',
        'Évora': 'Évora',
        'Faro': 'Faro',
        'Guarda': 'Guarda',
        'Leiria': 'Leiria',
        'Lisboa': 'Lisboa',
        'Portalegre': 'Portalegre',
        'Porto': 'Porto',
        'Santarém': 'Santarém',
        'Setúbal': 'Setúbal',
        'Viana do Castelo': 'Viana do Castelo',
        'Vila Real': 'Vila Real',
        'Viseu': 'Viseu',
        'Madeira':'Madeira',
        'Açores':'Açores'
    }
    STATUS = [(x, y) for y, x in distritos_dict.items()]
    distrito = models.CharField(max_length=20, choices=STATUS, default='')

    nota_primeiro_teste = models.DecimalField(max_digits = 4, decimal_places = 2, blank = True, null = True)

class Explicador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    ciclo_de_estudos = models.CharField(max_length=15, choices=[
    ('1', 'licenciatura'),
    ('2', 'mestrado'),
], default='')
    
    número_de_horas_disponíveis = models.IntegerField(default=0)
    
    
