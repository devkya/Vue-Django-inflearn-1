from django.urls import path, include

from . import views

app_name = 'api'
urlpatterns = [
    path('todo/list/', views.ApiTodoLV.as_view(), name='list'),
    path('todo/<int:pk>/delete/', views.ApiTodoDV.as_view(), name='delete'),
    path('todo/create/', views.ApiTodoCV.as_view(), name='create'),
    
]
