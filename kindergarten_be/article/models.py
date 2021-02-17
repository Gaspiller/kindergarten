from django.db import models

from user.models import UserProfile


class Article(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题')
    little_title = models.CharField(max_length=50, verbose_name='小标题')
    content = models.CharField(max_length=3000, verbose_name='正文')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default='')
    category = models.CharField(max_length=20, verbose_name='文章分类', default='')

    class Meta:
        db_table = 'article_article'
