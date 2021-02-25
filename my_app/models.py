from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Django ORM - Object Relational Mapper

class Post(models.Model):
    #o titulo será do tipo characteres de ate 255
    title = models.CharField(max_length=255)

    #O null é para o DB e o blank é para o formulario
    subtitle = models.CharField(max_length=255, null=True, blank=True)

    # o conteudo sera do tipo campo de texto, que nao terá limite de characteres
    content = models.TextField()

    #ao configurar o on_delete com PROTECT, se o user for deletado, seus posts nao serão excluidos
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class Meta:
    verbose_name = 'Artigo'
    #verbose_name_plural = 'Artigos

    def __str__(self):
        return self.title