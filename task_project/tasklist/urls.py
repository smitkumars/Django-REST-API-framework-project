from django.urls import path, include
from tasklist import views

urlpatterns=[
    path('',views.apioverview,name='apioverview'),
    path('task-list/',views.tasklistview,name='tasklistview'),
    path('task-detail/<str:pk>/',views.taskdetail,name='taskdetail'),
    path('task-create/',views.taskcreateview,name='taskcreateview'),
    path('task-update/<str:pk>/',views.taskupdateview,name='taskupdateview'),
    path('task-delete/<str:pk>/',views.taskdeleteview,name='taskdeleteview'),

]
