from django.db import models
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return str(self.name)

class Operation(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    cost = models.IntegerField()
    timestamp = models.DateTimeField(default=datetime.today)


    def __str__(self) -> str:
        return str(self.cost)
