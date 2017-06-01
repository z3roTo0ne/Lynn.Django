# coding=utf-8
from django.conf import settings


def my_setting(request):
    set_data = {
                'STATIC_URL': settings.STATIC_URL,
                'SITE_URL': settings.SITE_URL,        # URL前缀
                'SITE_NAME': settings.SITE_NAME,      # 站点名称
                }
    return set_data
