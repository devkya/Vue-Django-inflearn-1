from django.urls import include, path
from . import views

app_name = 'todo'

urlpatterns = [
    path('vonly/', views.TodoVueOnlyTV.as_view(), name='vonly'),
    
    path('create/', views.TodoCreateView.as_view(), name='create'),
    path('list/', views.TodoListView.as_view(), name='list'),
    path('<int:pk>/delete/', views.TodoDeleteView.as_view(), name='delete'),
    
    path('mixin/', views.TodoMOMCV.as_view(), name='mixin'),
    path('<int:pk>/delete2/', views.TodoDelV2.as_view(), name='delete2'),
]
