from uuid import uuid4
from django.db.models import Q 
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Message, User, Receiver
from django.core.exceptions import ValidationError


class MessageSerializator(serializers.ModelSerializer):
    message = serializers.CharField()
    class Meta:
        model = Message
        fields = ['message']


class ReceiverSerializer(serializers.ModelSerializer):
    receiver = serializers.CharField()
    user_token = serializers.CharField()
    class Meta:
        model = Receiver
        fields = ['receiver', 'user_token']


class UserSerializer(serializers.ModelSerializer):

    login = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    name = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(max_length=8)

    class Meta:
        model = User
        fields = (
            'login',
            'name',
            'password'
        )        

class UserLoginSerializer(serializers.ModelSerializer):

    login = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
  
        login = data.get("login", None)
        password = data.get("password", None)
        if not login and not password:
            raise ValidationError("Details not entered.")
        user = None
        user = User.objects.filter(
            Q(login=login) &
            Q(password=password)
        ).distinct()
        if not user.exists():
            raise ValidationError("User credentials are not correct.")
        user = User.objects.get(login=login)
        if user.ifLogged:
            raise ValidationError("User already logged in.")
        user.ifLogged = True
        data['token'] = uuid4()
        user.token = data['token']
        user.save()
        return data

    class Meta:
        model = User
        fields = (
            'login',
            'password',
            'token',
        )

        read_only_fields = (
            'token',
        )
