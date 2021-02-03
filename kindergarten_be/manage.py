#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kindergarten_be.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

#
# if __name__ == '__main__':
#     main()
#
# from django.db import models
# import random
#
#
# def default_sign():
#     signs = ['来吧，兄弟!', '快来吧，兄弟!']
#     return random.choice(signs)
#
#
# class UserProfile(models.Model):
#     username = models.CharField(max_length=12, verbose_name='用户名', primary_key=True)
#     nickname = models.CharField(max_length=30, verbose_name='昵称')
#     password = models.CharField(max_length=32)
#     email = models.EmailField()
#     phone = models.CharField(max_length=11)
#     coin = models.IntegerField(verbose_name="金币")
#     sign = models.CharField(max_length=50, verbose_name='个人签名', default=default_sign)
#     info = models.CharField(max_length=150, verbose_name='个人简介', default='')
#     created_time = models.DateTimeField(auto_now_add=True)
#     updated_time = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         db_table = 'user_user'
#
#
# import json
# from django.http import JsonResponse
# from django.views import View
# from .models import UserProfile
# import hashlib
#
#
# # 异常码 10100-10199
#
# class UserViews(View):
#
#     def get(self, request, username=None):
#         if username:
#             try:
#                 user = UserProfile.objects.get(username=username)
#             except Exception as e:
#                 result = {'code': 10102, 'error': '用户名错误'}
#                 return JsonResponse(result)
#
#         return JsonResponse({'code': 200, 'msg': '测试'})
#
#     def post(self, request):
#         json_str = request.body
#         json_obj = json.loads(json_str)
#
#         username = json_obj['username']
#         email = json_obj['email']
#         password_1 = json_obj['password_1']
#         password_2 = json_obj['password_2']
#         phone = json_obj['phone']
#
#         if password_1 != password_2:
#             result = {'code': 10100, 'error': '两次密码不一致'}
#             return JsonResponse(result)
#
#         old_users = UserProfile.objects.filter(username=username)
#         if old_users:
#             result = {'code': 10101, 'error': '用户名已存在'}
#             return JsonResponse(result)
#
#         p_m = hashlib.md5()
#         p_m.update(password_1.encode())
#         UserProfile.objects.create(username=username, nickname=username, password=p_m.hexdigest(), email=email,
#                                    phone=phone)
#
#         result = {'code': 200, 'username': username, 'data': {}}
#         return JsonResponse(result)
