from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题')
    little_title = models.CharField(max_length=50, verbose_name='小标题')
    content = models.CharField(max_length=3000, verbose_name='正文')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'article_article'
