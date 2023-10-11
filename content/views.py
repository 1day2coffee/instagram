from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from content.models import Feed


class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by("-id")
        return render(request, 'instagram/main.html', context=dict(feed_list=feed_list))

class UploadFeed(APIView):
    def post(self, request):
        file = request.data.get('file')
        image = request.data.get('image')
        content = request.data.get('content')
        profile_image = request.data.get('profile_image')
        user_id = request.data.get('user_id')


        print(file)
        print(image)
        print(content)
        print(profile_image)
        print(user_id)

        return Response(status=200)