from django.db import models

from config import settings

NULLABLE = dict(null=True, blank=True)

# Create your models here.
class Fruit(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self, ):
        return self.name
