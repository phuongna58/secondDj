from django.http import JsonResponse
from .models import Customer, Book, Author
from .serializers import CustomerSerializer, BookSerializer, AuthorSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
def cus_list(request):
    if request.method == 'GET':
        users = Customer.objects.all()
        serializer = CustomerSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def cus_detail(request, pk):
    try:
        user = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CustomerSerializer(user)
        return Response(serializer.data)
    elif request.method == 'POST' or request.method == 'PUT':
        serializer = CustomerSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        users = Book.objects.all()
        serializer = BookSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def author_list(request):
    if request.method == 'GET':
        users = Author.objects.all()
        serializer = AuthorSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
# def get_all_users(request):
#     cus = Customer.objects.all()  # Lấy toàn bộ bản ghi trong bảng User
#     serializer = CustomerSerializer(cus, many=True)  # Chuyển đổi danh sách các đối tượng User thành JSON
#     return JsonResponse(serializer.data, safe=False)


# @api_view(['POST'])
# def create_user(request):
#     serializer = CustomerSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)


# # from django.shortcuts import render
# from .models import Customer
# from rest_framework import serializers, viewsets
# from rest_framework.generics import (
#     ListCreateAPIView,
#     RetrieveUpdateDestroyAPIView)
# # Create your views here.


# class CusListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = '__all__'


# # API get detail, update, delete
# class CusDetailUpdateAPIView(viewsets.GenericViewSet,
#                               RetrieveUpdateDestroyAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CusListSerializer
#     lookup_field = 'id'
#     # permission_classes = [IsAuthenticated]
    
# class CusListCreateAPIView(viewsets.GenericViewSet,
#                             ListCreateAPIView):
#     serializer_class = CusListSerializer
#     queryset = Customer.objects.all()