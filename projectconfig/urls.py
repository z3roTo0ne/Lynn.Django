#! -*-coding:utf8 -*-
"""projectconfig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django_app.views import *
from django.contrib.auth.decorators import login_required
from rest_framework import routers
from api.views import *
from django.conf import settings
admin.autodiscover()

# AdminSite attributes的这个功能非常好，可以直接替换掉很多模板
# https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#overriding-admin-templates
# 会自动在你project的templates下面去寻找名字正确的template
admin.site.site_header = u"Django1.10 后台管理"
# admin.site.login_template = "login.html"
admin.site.site_title = "Django 后台管理"


# 给rest framework的view注册url
router = routers.DefaultRouter()
router.register(prefix=r'api/users', viewset=UserViewSet)
router.register(prefix=r'api/groups', viewset=GroupViewSet)


router.register(prefix=r'api/books', viewset=BookViewSet)
router.register(prefix=r'api/authors', viewset=AuthorViewSet)
router.register(prefix=r'api/publisher', viewset=PublisherViewSet)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dajax/', include('dajax.urls')),
    url(r'^api/', include('api.urls')),
    # url(r'^wife/', include('wife.urls'))
]

# django_app的url
urlpatterns += [
    url(r"^$", login_required(DisplayView.as_view(), login_url='/login/?next=/'), name='index'),
    url(r"^booklist/$", BookListView.as_view()),
    url(r"^duty/$", duty, name='duty'),
    url(r"^react/$", react, name='react'),
    url(r"^login/$", login, name='login'),
    url(r"^msg/$", msg, name='msg'),
    url(r"^create_user/$", CreateAuthorView.as_view(), name='create_user'),
    url(r"^search_book/$", search_book, name='search_book'),
    url(r"^change_book/$", change_book, name='change_book'),
    url(r"^delete_book/$", delete_book, name='delete_book'),
    url(r"^es6/$", es6, name='es6'),
    url(r"^angular/$", angular, name='angular'),

]


# REST framework的url
urlpatterns += [
    url(r'^', include(router.urls)),
    # 自动设置浏览器验证信息，不过django1.10以后已经不需要了， 可以不写下面这句
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^docs/', include('rest_framework_swagger.urls')),
]



# django document admin
urlpatterns += [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
]

# django oauth2
urlpatterns += [
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

# 通过event source来发送服务器事件
urlpatterns += [
    url(r'^event_source/',  event_source, name='event_source'),
    url(r'^real_msg/',  real_msg, name='real_msg'),
]

urlpatterns += [
    url(r'^test/', TestView.as_view(), name='test' )
]


urlpatterns += [
    url(r'cookie/show_user/', show_user, name='show-user'),
    url(r'cookie/set_user/', set_user, name='set-user'),
    url(r'session/show_session/', show_session, name='show-session'),
    url(r'session/set_session/', set_session, name='set-session'),
    url(r'session/del_session/', del_session, name='del-session')
    # name 是为了在template {%url "url-name" "url-parameter"%}
]

# debug tool bar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
