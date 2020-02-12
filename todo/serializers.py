"""
  @author : acoto
  @since : 11/2/20
  @Description : 
"""

from rest_framework import serializers
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class UserWithMail(UserCreationForm):
    username = forms.EmailField(label="Email address:")
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
