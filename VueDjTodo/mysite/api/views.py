from django.forms import model_to_dict
from django.views.generic.list import BaseListView
from django.views.generic.edit import BaseDeleteView, BaseCreateView

from todo.models import Todo
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

import json

# Create your views here.
class ApiTodoLV(BaseListView):
    model = Todo

    # def get(self, request, *args, **kwargs):
    #     tmpList = [
    #       {
    #         'id' : 1,
    #         'name': 'ㅇ김석훈',
    #         'todo': 'Django 와 Vue.js 연동 프로그램을 만들고 있습니다.'
    #       }, 
    #       {
    #         'id' : 2,
    #         'name': 'ㅇ홍길동',
    #         'todo': '이름을 안쓰면 홍길동으로 나와요...'
    #       }
    #     ]
    #     return JsonResponse(data=tmpList, safe=False)

    def render_to_response(self, context, **response_kwargs):
        todoList = list(context['object_list'].values())
        return JsonResponse(data=todoList, safe=False)

@method_decorator(ensure_csrf_cookie, name='dispatch')
class ApiTodoDV(BaseDeleteView):
    model = Todo
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse(data={}, status=204)
    
    
@method_decorator(ensure_csrf_cookie, name='dispatch')
class ApiTodoCV(BaseCreateView):
    model = Todo
    fields = '__all__'
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['data'] = json.loads(self.request.body)
        return kwargs
        
    def form_valid(self, form):
        self.object = form.save()
        newTodo = model_to_dict(self.object)
        print("newTodo : ", newTodo)
        return JsonResponse(data=newTodo, status=201)
    
    def form_invalid(self, form):
        return JsonResponse(data=form.errors, status=400)