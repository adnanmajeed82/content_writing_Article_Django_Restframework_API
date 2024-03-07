from django.db import models

class Writer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Category(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
