import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from tools.logging_dec import logging_check
from .models import UserProfile
import hashlib
from django.conf import settings


# 异常码 10100-10199

class UserViews(View):

    def get(self, request, username=None):
        if username:
            try:
                user = UserProfile.objects.get(username=username)
            except Exception as e:
                result = {'code': 10102, 'error': '用户名错误'}
                return JsonResponse(result)
            result = {'code': 200, 'username': username, 'data': {'info': user.info, 'sign': user.sign,
                                                                  'nickname': user.nickname}}
            return JsonResponse(result)

        return JsonResponse({'code': 200, 'msg': '测试'})

    def post(self, request):
        json_str = request.body
        json_obj = json.loads(json_str)

        username = json_obj['username']
        email = json_obj['email']
        password_1 = json_obj['password_1']
        password_2 = json_obj['password_2']
        phone = json_obj['phone']
        identity = json_obj['identity']

        if password_1 != password_2:
            result = {'code': 10100, 'error': '两次密码不一致'}
            return JsonResponse(result)

        old_users = UserProfile.objects.filter(username=username)
        if old_users:
            result = {'code': 10101, 'error': '用户名已存在'}
            return JsonResponse(result)

        old_phone = UserProfile.objects.filter(phone=phone)
        if old_phone:
            result = {'code': 10102, 'error': '号码已注册过'}
            return JsonResponse(result)

        p_m = hashlib.md5()
        p_m.update(password_1.encode())

        if identity:
            if identity == settings.TEACHER_PASS:
                UserProfile.objects.create(username=username, nickname=username, password=p_m.hexdigest(), email=email,
                                           phone=phone, is_teacher=True)
            else:
                result = {'code': 10103, 'error': '邀请码错误'}
                return JsonResponse(result)

        elif not identity:
            UserProfile.objects.create(username=username, nickname=username, password=p_m.hexdigest(), email=email,
                                       phone=phone, is_student=True)

        result = {'code': 200, 'username': username, 'data': {}}
        return JsonResponse(result)

    @method_decorator(logging_check)
    def put(self, request, username=None):
        json_str = request.body
        json_obj = json.loads(json_str)

        user = request.myuser
        user.sign = json_obj['sign']
        user.info = json_obj['info']
        user.nickname = json_obj['nickname']

        user.save()
        return JsonResponse({'code': 200})
