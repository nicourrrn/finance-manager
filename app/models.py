from django.db import models
from datetime import datetime

from .managers import ReversedManager


class Category(models.Model):
    name = models.CharField(max_length=50)
    ico = models.ImageField(upload_to='category_icons',
                            default='default.png')

    def __str__(self) -> str:
        return str(self.name)

class Operation(models.Model):
    short_description = models.CharField(max_length=50, default=None, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    cost = models.IntegerField()
    timestamp = models.DateTimeField(default=datetime.today)
    desctiption = models.TextField(default="")

    objects = ReversedManager()

    def __str__(self) -> str:
        resp = self.short_description
        if resp is None:
            resp = f"{self.category}: {self.cost}"
        return str(resp) 
