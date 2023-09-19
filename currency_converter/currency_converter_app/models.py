from django.db import models

class CurrencyRate(models.Model):
    currency_code = models.CharField(max_length=3, unique=True)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.currency_code} Rate: {self.exchange_rate}"

