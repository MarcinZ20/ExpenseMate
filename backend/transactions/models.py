from django.db import models
from root.settings import AUTH_USER_MODEL
from django.utils import timezone

class TransactionType(models.TextChoices):
    INCOME = "INCOME", 'Income'
    EXPENSE = "EXPENSE", 'Expense'

class TransactionCategories(models.TextChoices):
    FOOD_AND_RESTAURANTS = "FOOD", "Food & Restaurants"
    BILLS_AND_UTILITIES = "BILLS", "Bills & Utilities"
    TRANSPORTATION = "TRANSPORT", "Transportation"
    SHOPPING_AND_ENTERTAINMENT = "SHOPPING", "Shopping & Entertainment"
    HEALTH_AND_BEAUTY = "HEALTH", "Health & Beauty"
    EDUCATION_AND_DEVELOPMENT = "EDUCATION", "Education & Development"
    SAVINGS_AND_INVESTMENTS = "SAVINGS", "Savings & Investments"
    OTHER = "OTHER", "Other/Unexpected Expenses"

class Transaction(models.Model):
    '''An abstract class to model transaction.'''

    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.TextField(max_length=10, choices=TransactionType.choices)
    category = models.TextField(max_length=15, choices=TransactionCategories.choices, default=TransactionCategories.OTHER)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(blank=True, null=True, max_length=200)
    date = models.DateField()
    time = models.TimeField()

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def __str__(self) -> str:
        return f'Amount: {self.amount} on {self.description}'

    def save(self, *args, **kwargs):
        '''On save, update timestamp'''
        if not self.pk:
            self.created_at = timezone.now()
        
        self.updated_at = timezone.now()
        return super(Transaction, self).save()
    
    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
