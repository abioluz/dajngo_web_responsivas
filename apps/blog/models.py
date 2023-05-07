from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    autor = models.CharField(max_length=255)
    titlulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(default=datetime.now())