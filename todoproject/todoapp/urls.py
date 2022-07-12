from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:taskid>/', views.update, name='update'),
    path('cbview', views.tasklistview.as_view(), name="cbview"),
    path('cbdetail/<int:pk>/', views.taskdetailview.as_view(), name="cbdetail"),
    path('cbupdate/<int:pk>/', views.taskupdateview.as_view(), name="cbupdate"),
    path('cbdelete/<int:pk>/', views.taskdeleteview.as_view(), name="cbdelete"),

]
