import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from article.models import Article
from tools.logging_dec import logging_check


# 异常码：10300-10399

class ArticleViews(View):

    @method_decorator(logging_check)
    def post(self, request, username):
        username = request.myuser
        json_str = request.body
        json_obj = json.loads(json_str)
        title = json_obj['title']
        content = json_obj['content']
        little_title = json_obj['little_title']
        category = json_obj['category']
        Article.objects.create(title=title, content=content, username=username, little_title=little_title,
                               category=category)

        return JsonResponse({'code': 200})
