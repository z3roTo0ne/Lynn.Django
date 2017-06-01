# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from django_app.models import *
from common.custommixin import JSONResponseMixin
from django.views.generic import *
from django.core.serializers import serialize
from django.forms import ModelForm
from django import forms
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, StreamingHttpResponse
import csv, time
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.views.generic import DeleteView
from django.dispatch import Signal
from django.db.models.signals import pre_save
from django.core.signals import request_started, request_finished
import json, datetime
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.contrib import auth
import base64


class TestView(TemplateView):
    template_name = "test.html"

    def get(self, request, *args, **kwargs):
        pass


def show_user(request):
    html = ""
    print request.COOKIES
    if "username" in request.COOKIES:
        username = request.COOKIES['username']
        if username == "admin":
            html = u"用户{username}的Cookies没有超时".format(username=username)
        elif username == "snake":
            html = u"用户{username}的Cookies没有超时".format(username=username)
        else:
            dt = datetime.datetime.now() + datetime.timedelta(hours=int(1))
            name = "admin"
            html = u"用户{name}的Cookies已经超时, 设置用户{name}为登录回话,过去时间：{dt}".format(name=name,dt=dt)
            response = HttpResponse(html)
            response.set_cookie("username", name, expires=dt)
            return response
    response = HttpResponse(html)
    return response


def set_user(request, hour=1, user='admin'):
    dt = datetime.datetime.now() + datetime.timedelta(hours=int(hour))
    html = u"设置用户{user}登录, 过期时间为：{dt}".format(user=user, dt=dt)
    response = HttpResponse(html)
    response.set_cookie("username", user, expires=dt)
    return response


def show_session(request):
    html = None
    if "snake" in request.session:
        name = request.session["snake"]
        if name == "admin":
            html = u"得到一个session{name}".format(name=name)
        if not name:
            html = u"session为空"
        return HttpResponse(html)

    else:
        return HttpResponse(u"session为空")


def set_session(request, username="snake"):
    request.session.modified = True
    request.session.set_expiry(10)
    request.session['snake'] = username # 这就是保存了一个session, "snake就是session的key" session key和username别混了
    return HttpResponse(u"设置一个session")


def del_session(request):
    print request.session
    if "snake" in request.session:
        print u"会话ID是：{id}".format(id=request.session.session_key)
        del request.session
        return HttpResponse(u"清除一个session")
    return HttpResponse(u"没有session被清除")


class BookListView(ListView, JSONResponseMixin):
    model = Book
    # template_name = "index.html"
    # context_object_name = 'mybook'
    # 如果没有执行则默认规则是 [model_name]_list
    # paginate_by = 2
    template_name = None

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        # time = datetime.time()
        # context['time'] = time
        return serialize("json", context['object_list'])
        # return context

    # 如果没有指定get_queryset, 默认是 Book.objects.all()
    def get_queryset(self):
        # return Book.objects.get(id=2)
        return Book.objects.all()

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)


# def index(request):
#     return render(request, "index.html", locals())

class DisplayView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(DisplayView, self).get_context_data(**kwargs)
        return context


# class GetDataView(View):
#     def get(self, request):
#         data = "hehe"
#         if self.request.method == "GET":
#             obj = Author.objects.all()
#             data = serialize("json", obj)
#         return JsonResponse({'data': data})


def duty(request):
    return render(request, "duty.html", locals())


def react(request):
    return render(request, "react.html", locals())


def login(request):
    username = request.POST.get("username", None)
    password =  request.POST.get("password", None)
    remember = request.POST.get("remember-me", None)
    prefix = "fuck you mom".join(str(username))
    token = base64.encodestring(prefix)

    if request.POST and username and password:
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            response = HttpResponseRedirect("/")
            if remember == "on":
                response.set_cookie('username', username)
                response.set_cookie('password', password)
                response.set_cookie('token', token)
            messages.success(request, u"登录成功")
            return response
        else:
            messages.error(request, u"认证失败")
            return redirect("/login/")

    return render(request, "login.html", locals())


def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response


def msg(request):
    messages.add_message(request, messages.INFO, "hello world")
    messages.add_message(request, messages.DEBUG, "hello world")
    messages.add_message(request, messages.ERROR, "hello world")
    return render(request, "messages.html", locals())


class CreateAuthorView(SuccessMessageMixin, CreateView):
    template_name = 'author_form.html'
    fields = ('salutation', 'first_name', 'last_name', 'email', )
    model = Author
    success_url = '/create_user/'
    success_message = "user was created successfully"


# SSE的实时消息推送
def event_source(request):
    response = StreamingHttpResponse(stream_generator(request.user), content_type="text/event-stream")
    response['Cache-Control'] = 'no-cache'
    return response


def stream_generator(user):
    while True:
        # 读取当前用户的未读消息
        obj = Notify.objects.filter(user=user, read=False)
        data = serialize("json", obj)
        yield u"data: %s\n\n" % data
        time.sleep(10)


def real_msg(request):
    return render(request, "real_msg.html", locals())


def search_book(request):
    data = "hehe"
    return JsonResponse({"data": data})


def es6(request):
    return render(request, "es6.html", locals())

def angular(request):
    return render(request, "angular.html", locals())

@csrf_exempt
def change_book(request):
    if request.is_ajax() and request.method == "POST":
        data = json.loads(request.body)

        title = data.get('title').encode('utf-8')
        author = str(data.get('author')).encode('utf-8') # author 其实是多对多，前台传过来的是一个数组，这里只是测试，所以强制转str
        publisher = data.get('publisher').encode('utf-8')

        if data.has_key("id"):
            id = data.get("id")
            obj = get_object_or_404(Book, id=id)
            obj.title = title
            obj.authors.salutation = author
            obj.publisher.name = publisher
            obj.save()
            return JsonResponse({'data':'update ok'})
        else:
            publication_date = datetime.datetime.today()
            p = Book(title=title,
                     publisher=Publisher.objects.get(name=publisher),
                     publication_date=publication_date
                     )
            p.save()  #多对对字段保存的时候，要先save掉，然后去更新那个多对多字段
            p.authors.add(Author.objects.get(salutation=author))
            return JsonResponse({'data':'add ok'})

    return JsonResponse({'data':'ok'})


@csrf_exempt
def delete_book(request):
    if request.is_ajax() and request.method == "POST":
        data = json.loads(request.body)
        id = data.get("id")
        obj = get_object_or_404(Book, id=id)
        obj.delete()
        return JsonResponse({'data': 'delete ok'})

    return JsonResponse({'data': 'ok'})