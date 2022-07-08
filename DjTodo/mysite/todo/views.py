from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from .models import Todo
# Create your views here.
class TodoVueOnlyTV(TemplateView):
    template_name = 'todo/todo_vue_only.html'
    
    
class TodoCreateView(CreateView):
    model = Todo
    fields = '__all__'
    template_name = 'todo/todo_form.html'
    success_url = reverse_lazy('todo:list')
    

class TodoListView(ListView):
    model = Todo
    template_name = 'todo/todo_list.html'
    
    
class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo/todo_confirm_delete.html'
    success_url = reverse_lazy('todo:list')
    
    
class TodoMOMCV(MultipleObjectMixin, CreateView):
    model = Todo
    fields = '__all__'
    context_object_name = 'todo_list'
    template_name = 'todo/todo_form_list.html'
    success_url = reverse_lazy('todo:mixin')
    
    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.todo_list = self.get_queryset()
        return super().post(request, *args, **kwargs)
    
    
class TodoDelV2(DeleteView):
    model = Todo
    # template_name = 'todo/todo_confirm_delete.html'
    success_url = reverse_lazy('todo:mixin')
    
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    