from django.db import models

from users.models import CustomUser


class InvestmentAsset(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    ticker_symbol = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'INVESTMENT ASSET: {self.name}\n{self.description}'


class InvestmentTransaction(models.Model):
    BUY = 'buy'
    SELL = 'sell'
    DIVIDEND = 'dividend'
    INTEREST = 'interest'

    TYPE_CHOICES = [
        (BUY, 'Buy'),
        (SELL, 'Sell'),
        (DIVIDEND, 'Dividend'),
        (INTEREST, 'Interest'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    asset = models.ForeignKey(InvestmentAsset, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=6)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=6)
    transaction_date = models.DateField()
    currency = models.CharField(max_length=3, default='USD')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'INVESTMENT TRANSACTION: {self.asset.name} - {self.type} - {self.amount} {self.currency} on {self.transaction_date}'


class InvestmentPortfolio(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'INVESTMENT PORTFOLIO: {self.name}\n{self.description}'


class InvestmentPortfolioAsset(models.Model):
    portfolio = models.ForeignKey(InvestmentPortfolio, on_delete=models.CASCADE)
    asset = models.ForeignKey(InvestmentAsset, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('portfolio', 'asset')
