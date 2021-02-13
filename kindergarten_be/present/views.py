import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from tools.logging_dec import logging_check

# 异常码 10300-10399
from user.models import UserProfile


class PresentViews(View):
    @method_decorator(logging_check)
    def get(self):
        pass

    @method_decorator(logging_check)
    def post(self, request, shopname=None):
        json_str = request.body
        json_obj = json.loads(json_str)

        username = json_obj['username']
        shopname = json_obj['shopname']
        count = json_obj['count']
        price = json_obj['price']
        user = request.myuser
        coin = user.coin
        if coin < price * count:
            result = {'code': 10301, 'error': '金币不够'}
            return JsonResponse(result)
        else:
            coin = coin - price * count
            user.coin = coin
            user.save()
            result = {'code': 200}
            return JsonResponse(result)
