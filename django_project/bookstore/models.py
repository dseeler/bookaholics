from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=500)
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    card_num = models.CharField(max_length=16)
    card_exp = models.CharField(max_length=5)
    card_code = models.CharField(max_length=3)

    def __str__(self):
        return self.username
