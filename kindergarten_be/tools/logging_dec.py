from django.http import JsonResponse
import jwt
from django.conf import settings


def logging_check(func):
    def wrap(request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            result = {'code': 403, 'error': 'Please login'}
            return JsonResponse(result)
        try:
            res = jwt.decode(token, settings.JWT_TOKEN_KEY)
        except Exception as e:
            print('jwt decode erro is %s' % e)
            result = {'code': 403, 'error': 'Please login'}
            return JsonResponse(result)

        

        return func(request, *args, **kwargs)

    return wrap
