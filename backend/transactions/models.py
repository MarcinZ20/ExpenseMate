from django.db import models
from root.settings import AUTH_USER_MODEL
from django.utils import timezone

class Transaction(models.Model):
    '''An abstract class to model transaction.'''

    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(blank=True, null=True, max_length=200)
    date = models.DateField()
    time = models.TimeField()

    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def __str__(self) -> str:
        return f'Amount: {self.amount}'

    def save(self, *args, **kwargs):
        '''On save, update timestamp'''
        if not self.pk:
            self.created_at = timezone.now()
        
        self.updated_at = timezone.now()
        return super(Transaction, self).save()
    
    class Meta:
        abstract = True


class Expense(Transaction):
    '''A class that models user expense.'''

    recipient = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'Amount: {self.amount}, recipient: {self.recipient}'


class Income(Transaction):
    '''A class that models user income.'''

    source = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'Amount: {self.amount}, source: {self.source}'
