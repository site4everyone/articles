from django.db import models

# models of search app
class Article(models.Model):
  title = models.TextField()
  a_name = models.TextField()
  amount = models.IntegerField()
  payment= models.BooleanField(default=False)
  paid_to = models.CharField(max_length = 100)
