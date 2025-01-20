from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=5)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.code} ({self.name})'
