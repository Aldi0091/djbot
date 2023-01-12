from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import User
from .serializers import MessageSerializator, UserSerializer, UserLoginSerializer, ReceiverSerializer


class Register(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Login(generics.GenericAPIView):

    # queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLoginSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


class Message(generics.GenericAPIView):
    serializer_class = MessageSerializator
    def post(self, request, *args, **kwargs):
        serializer_class = MessageSerializator(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


class Receiver(generics.GenericAPIView):
    serializer_class = ReceiverSerializer
    def post(self, request, *args, **kwargs):
        serializer_class = ReceiverSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):        
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


# def index(request):
#     return redirect('/api/login')



