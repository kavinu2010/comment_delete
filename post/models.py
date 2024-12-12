from django.db import models

# Create your models here.
class Poster(models.Model):
  title=models.CharField(max_length=200)
  comment=models.TextField()

  def __str__(self):
    return f'{self.title}-{self.comment}'