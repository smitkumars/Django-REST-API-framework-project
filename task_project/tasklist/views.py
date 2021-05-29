from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import taskSerializer
from .models import task
# Create your views here.
@api_view(['GET'])
def apioverview(request):
    api_urls={'List':'/task-list/',
            'Datail view':'/task-detail/<str:pk>/',
            'Create':'/task-create/',
            'Update':'/task-update/<str:pk>/',
            'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def tasklistview(request):
    task1=task.objects.all()
    serializer=taskSerializer(task1,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskdetail(request,pk):
    task1=task.objects.get(id=pk)
    serializer=taskSerializer(task1,many=False)
    return Response(serializer.data)







@api_view(['POST'])
def taskcreateview(request):
    serializer=taskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def taskupdateview(request,pk):
    task1=task.objects.get(id=pk)
    serializer=taskSerializer(instance=task1, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskdeleteview(request,pk):
    task1=task.objects.get(id=pk)
    task1.delete()

    return Response("Item successfully deleted")
