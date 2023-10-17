from django.shortcuts import render
from rest_framework.views import APIView

class Main(APIView):
    def get(self, request):
        print("request get")
        return render(request, "instagram/main.html")