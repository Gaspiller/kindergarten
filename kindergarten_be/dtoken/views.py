import json
import time

import jwt
from django.http import JsonResponse
from user.models import UserProfile
import hashlib
from django.conf import settings


# 异常码 10200-10299

def tokens(request):
    if request.method != 'POST':
        result = {'code': 10200, 'error': '请登录'}
        return JsonResponse(result)
    json_str = request.body
    json_obj = json.loads(json_str)
    username = json_obj['username']
    password = json_obj['password']

    try:
        user = UserProfile.objects.get(username=username)
    except Exception as e:
        result = {'code': 10201, 'error': '用户名或密码错误'}
        return JsonResponse(result)
    p_m = hashlib.md5()
    p_m.update(password.encode())
    if p_m.hexdigest() != user.password:
        result = {'code': 10202, 'error': '用户名或密码错误'}
        return JsonResponse(result)
    token = make_token(username)
    # user = UserProfile.objects.get(username=username)
    identity = user.identity
    result = {'code': 200, 'username': username, 'identity': identity, 'data': {'token': token.decode()}}
    return JsonResponse(result)


def make_token(username, expire=3600 * 24):
    key = settings.JWT_TOKEN_KEY
    now_t = time.time()
    payload_data = {'username': username, 'exp': now_t + expire}
    return jwt.encode(payload_data, key, algorithm='HS256')
