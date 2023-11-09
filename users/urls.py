from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path("", views.CustomUserListView.as_view(), name='users'),
]