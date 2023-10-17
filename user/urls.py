from django.urls import path
from .views import Join, Login
from content.views import Main

urlpatterns = [
    path('join', Join.as_view(), name='join'),
    path('login', Login.as_view(), name='login'),
    path('main', Main.as_view(), name='main')
]