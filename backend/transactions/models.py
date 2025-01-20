import uuid

from django.db import models

from users.models import CustomUser


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'name')
        indexes = [
            models.Index(fields=['user', 'name'])
        ]

    def __str__(self):
        return f'CATEGORY: {self.name}\n{self.description}'


class Budget(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'BUDGET: {self.category.name} - {self.amount} {self.currency} from {self.start_date} to {self.end_date}'


class Transaction(models.Model):
    EXPENSE = 'expense'
    INCOME = 'income'

    TYPE_CHOICES = [
        (EXPENSE, 'Expense'),
        (INCOME, 'Income'),
    ]

    CARD = 'card'
    CASH = 'cash'
    BANK = 'bank'
    OTHER = 'other'

    TRANSACTION_METHOD_CHOICES = [
        (CARD, 'Card'),
        (CASH, 'Cash'),
        (BANK, 'Bank'),
        (OTHER, 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField()
    transaction_method = models.CharField(max_length=10, choices=TRANSACTION_METHOD_CHOICES, default=CASH)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=EXPENSE)
    currency = models.CharField(max_length=3, default='USD')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['user', 'transaction_date']),
            models.Index(fields=['user', 'category'])
        ]

    def __str__(self):
        return f"{self.type.capitalize()} - {self.amount} {self.currency}"


class RecurringTransaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.DurationField()
    next_due_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'RECURRING TRANSACTION: {self.category.name} - {self.amount} every {self.frequency} on {self.next_due_date}'


class IncomeSource(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'INCOME SOURCE: {self.name}\n{self.description}'
