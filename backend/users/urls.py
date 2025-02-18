from django.urls import path
from .views import UserDetailView, ListUsersView


urlpatterns = [
    path('users/', ListUsersView.as_view(), name='list_users_view'),
    path('users/<int:id>/profile/', UserDetailView.as_view(), name='user_detail_view'),
]