from django.conf.urls import url
from dajax.views import *

urlpatterns = [
    # url(r'^ajax_request/$', AjaxModelHandler, name='ajax_request'),
    url(r"^getdata/$", GetModelListView.as_view(), name='getdata'),
]