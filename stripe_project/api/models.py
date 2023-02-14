from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_price_in_dollars(self):
        return self.price / 100
