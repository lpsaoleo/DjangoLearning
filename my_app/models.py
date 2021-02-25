from django.db import models

# Create your models here.
#Django ORM - Object Relational Mapper

class Post(models.Model):
    #o titulo será do tipo characteres de ate 255
    title = models.CharField(max_length=255)

    #o conteudo sera do tipo campo de texto, que nao terá limite de characteres
    subtitle = models.CharField(max_length=255, null=True)
    content = models.TextField()
