from django.http import JsonResponse

#异常码 10200-10299

def tokens(request):
    if request.method != 'POST':
        result = {'code':10200,'error':'请登录'}
        return JsonResponse(result)

    result = {'code': 200, 'error': '请登录'}
    return JsonResponse(result)