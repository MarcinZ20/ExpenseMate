from django.urls import path
from .views import UserTransactionsListView

urlpatterns = [
    path('users/<int:id>/transactions/', UserTransactionsListView.as_view(), name='user_transactions'),
]