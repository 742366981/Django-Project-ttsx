from django.db import models


class MainWheel(models.Model):
    img = models.CharField(max_length=200)
    name=models.CharField(max_length=16)

    class Meta:
        db_table = 'main_wheel'


class MainAdv(models.Model):
    img = models.CharField(max_length=200)
    name=models.CharField(max_length=16)

    class Meta:
        db_table = 'main_adv'


class GoodsType(models.Model):
    gt_id = models.CharField(max_length=16)
    gt_name = models.CharField(max_length=16)
    clas=models.CharField(max_length=200)
    img=models.CharField(max_length=255)

    class Meta:
        db_table = 'goods_type'


class Goods(models.Model):
    g_id=models.CharField(max_length=16)
    img=models.CharField(max_length=255)
    price=models.FloatField(default=0)
    name=models.CharField(max_length=40)
    gt=models.ForeignKey(GoodsType)

    class Meta:
        db_table = 'goods'


