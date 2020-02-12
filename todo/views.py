# Django
from django.contrib.auth.models import User

# Provider OAuth2
from provider.oauth2.models import Client

# Todo App
from .serializers import RegistrationSerializer, UserSerializer,UserWithMail

# rest
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from django.shortcuts import render

class RegistrationView(APIView):
    permission_classes = ()

    def post(self, request):
        serializer = RegistrationSerializer(data=request.DATA)
        if not serializer.is_valid():
            return Response(serializer.errors, \
                            status=status.HTTP_400_BAD_REQUEST)

        data = serializer.data
        u = User.objects.create(username=data['username'], email=data['email'])
        u.set_password(data['password'])
        u.save()
        name = u.username
        client = Client(user=u, name=name, url='' + name, \
                        client_id=name, client_secret='', client_type=1)
        client.save()

        return Response(serializer.data, status=201)


class UserModelView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        umodel = User.objects.filter(username=request.user.username)
        serializer = UserSerializer(umodel, many=True)
        return Response(serializer.data)


def signup(request):
    return render(request, 'signup.html')
