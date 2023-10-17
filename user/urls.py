from django.urls import path
from .views import Join, Login, LogOut
from instagram.views import Profile
from content.views import Main

urlpatterns = [
    path('join', Join.as_view(), name='join'),
    path('login', Login.as_view(), name='login'),
    path('main', Main.as_view(), name='main'),
    path('logout', LogOut.as_view(), name='logout'),
    path('profile', Profile.as_view(), name='profile')
]