from django.db import models

# Create your models here.
CHOICES_ASSUNTO = [
    ('', 'Selecione um assunto'),
    ('descontos', 'Descontos'),
    ('consultoria', 'consultoria'.capitalize()),
    ('freelance', 'freelance'.capitalize()),
    ('elogios', 'elogios'.capitalize()),
    ('reclamações', 'reclamações'.capitalize()),
    ('outros', 'outros'.capitalize()),

]


class Contato(models.Model):
    assunto = models.CharField(choices=CHOICES_ASSUNTO, default='', max_length=100)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mensagem = models.CharField(max_length=1000)
