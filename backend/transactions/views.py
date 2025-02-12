import django_filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

from .models import Transaction
from .serializers import TransactionSerializer

class TransactionPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100
    page_size_query_param = 'page_size'    


class TransactionFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='date', lookup_expr='lte')
    min_amount = django_filters.NumberFilter(field_name='amount', lookup_expr='gte')
    max_amount = django_filters.NumberFilter(field_name='amount', lookup_expr='lte')
    exact_amount = django_filters.NumberFilter(field_name='amount', lookup_expr='exact')
    
    class Meta:
        model = Transaction
        fields = ['date', 'amount']

class UserTransactionsListView(ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication, ]
    pagination_class = TransactionPagination

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = TransactionFilter
    ordering_fields = ['date', 'amount']

    def get_queryset(self):
        user_id = self.kwargs['id']
        return Transaction.objects.filter(user=user_id)