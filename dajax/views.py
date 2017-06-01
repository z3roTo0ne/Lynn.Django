# -*- coding: utf-8 -*-
from common.custommixin import JSONResponseMixin
from django.views.generic import ListView
from django_app.models import *
from django.core.serializers import serialize
# from django.core.wsgi import


class GetModelListView(ListView, JSONResponseMixin):
    model = Book
    template_name = None

    def get_context_data(self, **kwargs):
        context = super(GetModelListView, self).get_context_data(**kwargs)
        return serialize("json", context['object_list'])

    # 如果没有指定get_queryset, 默认是 Book.objects.all()
    def get_queryset(self):
        # return Book.objects.get(id=2)
        # for key, value in self.request.GET.items():
        #     print key
        return Book.objects.all()

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)