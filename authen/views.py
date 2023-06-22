from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserLoginSerializer, UserRegisterSerializer
from django.contrib.auth.models import User


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            # Tạo tài khoản người dùng mới
            # Bạn có thể sử dụng Django's User model hoặc một model người dùng tùy chỉnh
            # Ví dụ:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            # rs = {}
            # rs['a'] = 12367
            # rs['b'] = "abcd"
            return Response({'message': 'Đăng ký thành công', 'abcd': "deff"}, status=status.HTTP_201_CREATED)
            # return Response(rs, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
