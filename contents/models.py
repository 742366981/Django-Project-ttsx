from django.db import models

from users.models import User


# 轮播
class MainWheel(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=16)

    class Meta:
        db_table = 'main_wheel'


# 轮播右侧图
class MainAdv(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=16)

    class Meta:
        db_table = 'main_adv'


# 商品类型
class GoodsType(models.Model):
    gt_id = models.CharField(max_length=16)
    gt_name = models.CharField(max_length=16)
    clas = models.CharField(max_length=200)
    img = models.CharField(max_length=255)

    class Meta:
        db_table = 'goods_type'


# 商品
class Goods(models.Model):
    g_id = models.CharField(max_length=16)
    img = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    name = models.CharField(max_length=40)
    gt = models.ForeignKey(GoodsType)

    class Meta:
        db_table = 'goods'


# 购物车
class Cart(models.Model):
    user = models.ForeignKey(User)  # 关联用户
    goods = models.ForeignKey(Goods)  # 关联商品
    c_num = models.IntegerField(default=1)  # 商品的个数
    is_select = models.BooleanField(default=True)  # 是否选择商品

    class Meta:
        db_table = 'cart'


# 收货地址
class Address(models.Model):
    recipient = models.CharField(max_length=20)
    detail_address = models.CharField(max_length=100)
    post_code = models.IntegerField(null=True)
    tel = models.CharField(max_length=11)
    user = models.ForeignKey(User)
    is_select=models.BooleanField(default=False)

    class Meta:
        db_table = 'address'


# 订单
class Order(models.Model):
    user = models.ForeignKey(User)  # 关联用户
    o_num = models.CharField(max_length=64)  # 订单号
    # 0 代表已下单，但是未付款， 1 已付款
    o_status = models.IntegerField(default=0)  # 状态
    o_create = models.DateTimeField(auto_now_add=True)  # 创建时间

    class Meta:
        db_table = 'order'


# 提交订单后的商品
class OrderGoods(models.Model):
    goods = models.ForeignKey(Goods)  # 关联的商品
    order = models.ForeignKey(Order)  # 关联的订单
    goods_num = models.IntegerField(default=1)  # 商品的个数

    class Meta:
        db_table = 'order_goods'
