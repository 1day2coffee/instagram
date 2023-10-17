from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User


# Create your views here.
class Join(APIView):
    def get(self, request):
        return render(request, "user/join.html")

    def post(self, request):
        email = request.data.get('email', None)
        user_id = request.data.get('user_id', None)
        name = request.data.get('name', None)
        password = request.data.get('password', None)

        User.objects.create(email=email, user_id=user_id, name=name, password=password)

        return Response(status=200)


class Login(APIView):
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        User.objects.create(email=email, password=password)

        return Response(status=200)