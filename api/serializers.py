#! -*- coding:utf8 -*-
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django_app.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.SlugRelatedField(
        many=True,  # 只有manytomany字段才可以true
        read_only=True,
        slug_field='salutation'  # 外键的字段显示的名称
    )

    publisher = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Book
        fields = ('id', 'title', 'authors', 'publisher', 'publication_date')
