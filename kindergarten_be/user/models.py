from django.db import models
import random


def default_sign():
    signs = ['来吧，兄弟!', '快来吧，兄弟!']
    return random.choice(signs)


class UserProfile(models.Model):
    username = models.CharField(max_length=12, verbose_name='用户名', primary_key=True)
    nickname = models.CharField(max_length=30, verbose_name='昵称')
    password = models.CharField(max_length=32)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    coin = models.IntegerField(verbose_name="金币")
    sign = models.CharField(max_length=50, verbose_name='个人签名', default=default_sign)
    info = models.CharField(max_length=150, verbose_name='个人简介', default='')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'
