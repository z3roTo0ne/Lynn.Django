#! -*- coding:utf8 -*-
from django.contrib.auth.models import User, Group
from api.serializers import *
from django_app.models import *
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.core.exceptions import FieldError
from rest_framework import filters, generics, viewsets, views, renderers, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view


class UserViewSet(viewsets.ModelViewSet):
    """
    用户信息的api接口集
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    用户组信息的api的接口集
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ManageUser(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # 接口权限控制
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

    def get(self, request, *args, **kwargs):
        """
        获取用户信息
        """
        query_condition = self.request.GET
        q = Q()
        for i in query_condition:
            if i == "format":
                continue
            q.add(Q(**{i: query_condition[i]}), Q.OR)
        try:
            users = User.objects.filter(q)
        except FieldError:
            return JsonResponse({'ERROR': 'invalid query condition!'})

        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        创建、修改、删除用户
         curl -w %{http_code} -l -H "Content-type: application/json" -X POST  -u admin:chenlin1989 -d '{"username":"snakechen"}' http://192.168.102.128:8000/api/manage_user/
        """
        serializer = UserSerializer(data=self.request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def permission_denied_handler(request):
    return HttpResponse('you have no permissions!')

