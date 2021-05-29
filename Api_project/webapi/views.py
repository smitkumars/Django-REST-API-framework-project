from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from webapi.models import employees
from .serializers import employeesSerializer


class employeeList(APIView):
    def get(self,request):
        employee1=employees.objects.all()
        serializer=employeesSerializer(employee1,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=employeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
