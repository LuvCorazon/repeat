from django.db import models

class category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(product, on_delete=models.CASCADE)
