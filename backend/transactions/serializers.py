from rest_framework import serializers
from .models import Transaction, Budget, Category, IncomeSource, RecurringTransaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            'user',
            'category',
            'amount',
            'transaction_date',
            'transaction_method',
            'type',
            'currency',
            'description',
        )
        read_only_fields = ('user',)

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount cannot be negative or zero.")
        return value


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = (
            'user',
            'category',
            'amount',
            'currency',
            'start_date',
            'end_date',
        )
        read_only_fields = ('user',)


    def validate_amount(self, value):
            if value < 0:
                raise serializers.ValidationError("Amount cannot be negative.")
            return value


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
            'description',
        )


class IncomeSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeSource