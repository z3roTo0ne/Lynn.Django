#! -*- coding:utf8 -*-
from django.conf.urls import url
from api.views import ManageUser

urlpatterns = [
    url(r'^manage_user/', ManageUser.as_view())
]