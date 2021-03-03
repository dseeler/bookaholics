from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=500)
    year = models.CharField(max_length=4)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=10.00)

    def __str__(self):
        return self.title
