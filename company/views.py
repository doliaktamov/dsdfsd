from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Company, Category, Product
# from .serializers import GenreSerializer, MovieSerializer
from django.urls import reverse
from rest_framework import status
from django.utils.translation import gettext as _
from rest_framework.views import APIView
from django.forms.models import model_to_dict
import json
from .serializers import ProductSerializer, CompanySerializer, CategorySerializer
from rest_framework.viewsets import ModelViewSet, ViewSet

class CompanyView(APIView):

    def get(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailCompanyView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Company, pk=pk)

    def get(self, request, pk):
        serializer = CompanySerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = CompanySerializer(self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.sata)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductSerializer.object.all()


@api_view(['GET'])
def category_view(request):
    if request.method == "GET":
        company = CategorySerializer.objects.all()
        serializer = CategorySerializer(company)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def category_detail(request, pk):
    obj = get_object_or_404(Category, pk=pk)

    if request.method == "GET":
        serializer = CategorySerializer(obj)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = CategorySerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    if request.method == "DELETE":
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

