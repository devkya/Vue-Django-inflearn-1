# (Inflearn) Vue.js - Django 연동 웹 프로그래밍

[강의 링크](https://www.inflearn.com/course/vue-js-2/dashboard)

## HTML로 todo 앱 코딩

- booktodo.html
  - script 최신 버전으로 변경해야 함

## Vue.js로 todo 앱 코딩

### URL 설계

| URL pattern      | View Name                                  | template Name            |
| ---------------- | ------------------------------------------ | ------------------------ |
| /admin/          | 장고 기본 제공                             |                          |
| /todo/vonly/     | TodoVueOnlyTV(TemplateView)                | todo_vue_only.html       |
|                  |                                            |                          |
| /todo/create/    | TodoCreateView(CreateView)                 | todo_form.html           |
| /todo/list/      | TodoListView(ListView)                     | todo_list.html           |
| /todo/99/delete/ | TodoDeleteView(DeleteView)                 | todo_confirm_delete.html |
| /todo/mixin/     | TOdoMOMCV(MultipleObjectMixin, CreateView) | tofo_form_list.html      |
| /todo/99/delete2 | TodoMixinDelV(DeleteView)                  | 팝업창                   |

### 내용

- Django로 뼈대를 구축하고 template 사용
- 양방향 통신 안됨
- save() 오버라이딩을 통하여 다른 작업을 실행 후 저장
- super().save() 를 통한 db 저장

```python
def save(self):
    if not self.name:
        self.name = "devKya"
    super().save()
```

### CDN 골격잡기

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Document</title>
    <!-- 
    bootstrap.css, 
    fontawesome.css, 
    not glyphicon favicon.ico -->
  </head>

  <body>
    <!-- 
    jquery.js 
    popper.js
    bootstrap.js -->
  </body>
</html>
```

## Mixin

- 두 개의 view를 상속 받을 때는 더 복잡한 view 부터 상속받는게 좋음
- (mixin, main)

## Vue-Django 연동

1. 척 페이지는 장고에서 생성해서 클라이언트에게 보내줌
2. 이후 화면 렌더링은 Vue.js 에서 수행
3. 데이터 저장은 서버측 DB 저장
4. Client-Server 간 Data 연동은 json 포맷으로 함
5. Vue.js 의 directive/axios 기능 사용
6. DRF 대신에 JsonResponse 사용

| URL pattern          | View Name                 | template Name                     |
| -------------------- | ------------------------- | --------------------------------- |
| /admin/              | (장고 기본 제공)          |                                   |
| /                    | HomeView(TemplateView)    | home.html                         |
|                      |                           |                                   |
| /todo/               | TodoTV(TemplateView)      | todo_index.html(Vue.js 코드 포함) |
|                      |                           |                                   |
| /api/todo/list/      | ApiTodoLV(BaseListView)   | (불필요)                          |
| /api/todo/create/    | ApiTodoCV(BaseCreateView) | (불필요)                          |
| /api/todo/99/delete/ | ApiTodoDV(BaseDeleteView) | (불필요)                          |

- Vue-Django Json 연동방식
  ![django-vue](./%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C.png)

- BaseListView vs ListView
  ListView 에서는 Template rendering에 대한 것을 포함하기에, API 사용시 BaseListView가 더 좋음

* csrf-token
  server는 csrf token을 생성해서 클라이언트(브라우저)에게 보내주고, 브라우저는 쿠키에 저장
  Vue.js 에서는 쿠키를 찾아 요청 헤더에 넣어 서버로 보냄
  이떄 django와 vue는 이름을 맞춰줘야 함
