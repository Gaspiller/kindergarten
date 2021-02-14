from django.db import models
from user.models import UserProfile


class Present(models.Model):
    shopname = models.CharField(max_length=30, verbose_name='商品名称')
    price = models.IntegerField(verbose_name='商品价格')
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default='')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'present_present'
