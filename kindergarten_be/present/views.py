import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View

from present.models import Present
from tools.logging_dec import logging_check


# 异常码 10300-10399


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
        shopcount = int(json_obj['shopcount'])
        price = int(json_obj['price'])
        user = request.myuser
        coin = int(user.coin)
        if coin < price * shopcount:
            result = {'code': 10301, 'error': '金币不够'}
            return JsonResponse(result)
        else:
            coin = coin - price * shopcount
            user.coin = coin
            Present.objects.create(shopname=shopname, price=price, buyer=user)
            user.save()
            result = {'code': 200}
            return JsonResponse(result)
