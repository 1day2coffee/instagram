import os
from uuid import uuid4

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from content.models import Feed
from instagram.settings import MEDIA_ROOT
from user.models import User


class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by("-id")

        email = request.session.get('email', None)

        if email is None:
            return render(request, "user/login.html")

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, "user/login.html")

        return render(request, 'instagram/main.html', context=dict(feed_list=feed_list, user=user))

class UploadFeed(APIView):
    def post(self, request):
        file = request.FILES['file']
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        content = request.data.get('content')
        image = uuid_name
        profile_image = request.data.get('profile_image')
        user_id = request.data.get('user_id')

        Feed.objects.create(content=content, image=image, profile_image=profile_image, user_id=user_id, like_count=0)

        return Response(status=200)