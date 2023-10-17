from django.shortcuts import render
from rest_framework.views import APIView

class Sub(APIView):
    def get(self, request):
        print("request get")
        return render(request, "instagram/main.html")

class Profile(APIView):
    def get(self, request):
        return render(request, 'instagram/profile.html')