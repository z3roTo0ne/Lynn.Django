from tastypie.resources import ModelResource
from django_app.models import *


class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        allowed_methods = ['get']

