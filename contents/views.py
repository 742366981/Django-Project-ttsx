from random import randrange

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse

from contents.models import MainWheel, MainAdv, Goods, GoodsType, Cart, Address, Order, OrderGoods

# 首页
from utils.functions import get_order_num


def index(request):
    if request.method == 'GET':
        gts = GoodsType.objects.all()
        wheels = MainWheel.objects.all()
        advs = MainAdv.objects.all()
        goods = Goods.objects.all()
        return render(request, 'contents/index.html', {'wheels': wheels,
                                                       'advs': advs,
                                                       'goods': goods,
                                                       'gts': gts})


# 购物车
def cart(request):
    if request.method == 'GET':
        user = request.user
        if user.id:
            carts = Cart.objects.filter(user=user)
        return render(request, 'contents/cart.html', {'carts': carts})


# 商品详情
def detail(request, tid, gid):
    if request.method == 'GET':
        gts = GoodsType.objects.all()
        # 随机选取2个推荐商品
        rgoods = Goods.objects.all()
        i = randrange(len(rgoods))
        rgoods = rgoods[i:i + 2]
        gt = GoodsType.objects.get(gt_id=tid)
        good = Goods.objects.filter(g_id=gid, gt=gt).first()
        return render(request, 'contents/detail.html',
                      {'good': good, 'tid': tid, 'gid': gid, 'gts': gts, 'rgoods': rgoods})


# 跳转全部商品列表页
def listre(request):
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('contents:list', kwargs={'tid': '1000', 'sid': 0}))


# 商品列表
def list(request, tid, sid):
    if request.method == 'GET':
        # 随机选取2个推荐商品
        rgoods = Goods.objects.all()
        i = randrange(len(rgoods))
        rgoods = rgoods[i:i + 2]
        gts = GoodsType.objects.all()
        if tid == '1000':
            if sid == '0':
                goods = Goods.objects.order_by('name')
            if sid == '1':
                goods = Goods.objects.order_by('price')
            if sid == '2':
                goods = Goods.objects.order_by('-price')
        else:
            gtss = GoodsType.objects.get(gt_id=tid)
            goods = Goods.objects.filter(gt=gtss)
            if sid == '0':
                goods = goods.order_by('name')
            if sid == '1':
                goods = goods.order_by('price')
            if sid == '2':
                goods = goods.order_by('-price')

        return render(request, 'contents/list.html',
                      {'tid': tid, 'gts': gts, 'goods': goods, 'rgoods': rgoods, 'sid': sid})


# 支付
def place_order(request):
    if request.method == 'GET':
        user = request.user
        if user.id:
            address = Address.objects.filter(user=user)
            carts = Cart.objects.filter(user=user, is_select=True)
            return render(request, 'contents/place_order.html', {'address': address, 'carts': carts})


# 个人信息
def user_center_info(request):
    if request.method == 'GET':
        user = request.user
        if user.id:
            username = user.username
            address = Address.objects.filter(user=user, is_select=True).first()
            all_goods = Goods.objects.all()
            recent_goods = all_goods[len(all_goods) - 5:len(all_goods)]
            return render(request, 'contents/user_center_info.html', {'username': username, 'address': address,
                                                                      'recent_goods': recent_goods})


# 全部订单
def user_center_order(request):
    if request.method == 'GET':
        user = request.user

        no_pay_orders = Order.objects.filter(user=user, o_status=0)

        yes_pay_orders = Order.objects.filter(user=user, o_status=1)

        return render(request, 'contents/user_center_order.html', {'no_pay_orders': no_pay_orders,
                                                                   'yes_pay_orders': yes_pay_orders})


# 收货地址
def user_center_site(request):
    if request.method == 'GET':
        user = request.user
        if user.id:
            address = Address.objects.filter(user=user, is_select=True).first()
            other_address = Address.objects.filter(user=user, is_select=False)
            return render(request, 'contents/user_center_site.html',
                          {'address': address, 'other_address': other_address})
    if request.method == 'POST':
        user = request.user
        if user.id:
            recipient = request.POST.get('recipient')
            detail_address = request.POST.get('detail_address')
            post_code = request.POST.get('post_code')
            tel = request.POST.get('tel')
            Address.objects.create(recipient=recipient, detail_address=detail_address, post_code=post_code,
                                   tel=tel, user=user)
            return HttpResponseRedirect(reverse('contents:placeOrder'))


# 添加商品
def add_cart(request):
    if request.method == 'POST':
        user = request.user
        data = {}
        data['code'] = 1001
        if user.id:
            g_id = request.POST.get('g_id')
            cart = Cart.objects.filter(user=user, goods_id=g_id).first()
            if cart:
                cart.c_num += 1
                cart.save()
                data['c_num'] = cart.c_num
            else:
                Cart.objects.create(user=user, goods_id=g_id)
                data['c_num'] = 1
            data['code'] = 200
            data['msg'] = '请求成功'
            return JsonResponse(data)
        return JsonResponse(data)


# 减少商品
def reduce_cart(request):
    if request.method == 'POST':
        user = request.user
        data = {}
        if user.id:
            g_id = request.POST.get('g_id')
            cart = Cart.objects.filter(user=user, goods_id=g_id).first()
            if not cart:
                pass
            else:
                if cart.c_num == 1:
                    cart.delete()
                    data['c_num'] = 0
                    data['code'] = 200
                else:
                    cart.c_num -= 1
                    cart.save()
                    data['c_num'] = cart.c_num
                    data['code'] = 200
            return JsonResponse(data)


# 获得购物车商品信息
def get_price(request):
    if request.method == 'GET':
        user = request.user
        if user.id:
            carts = Cart.objects.filter(user=user)
            prices = 0
            counts = 0
            for cart in carts:
                if cart.is_select:
                    prices += cart.goods.price * cart.c_num
                    counts += cart.c_num
            prices = '%.2f' % prices
            return JsonResponse({'prices': prices, 'counts': counts})


# 改变购物车商品状态
def change_status(request):
    if request.method == 'POST':
        user = request.user
        if user.id:
            g_id = request.POST.get('g_id')
            cart = Cart.objects.filter(user=user, goods_id=g_id).first()
            if cart.is_select:
                cart.is_select = False
                cart.save()
            else:
                cart.is_select = True
                cart.save()
            return JsonResponse({'code': 200, 'is_select': cart.is_select})


# 全选
def all_status(request):
    if request.method == 'POST':
        user = request.user
        if user.id:
            carts = Cart.objects.all()
            for cart in carts:
                cart.is_select = True
                cart.save()
            return JsonResponse({'code': 200})


# 删除商品
def good_delete(request):
    if request.method == 'POST':
        user = request.user
        if user.id:
            g_id = request.POST.get('g_id')
            cart = Cart.objects.filter(user=user, goods_id=g_id).first()
            cart.delete()
            return JsonResponse({'code': 200})


# 获得详情页商品价格
def get_a_price(request):
    if request.method == 'POST':
        user = request.user
        data = {}
        if user.id:
            g_id = request.POST.get('g_id')
            cart = Cart.objects.filter(user=user, goods_id=g_id).first()
            if cart:
                price = cart.c_num * cart.goods.price
                price = '%.2f' % price
                data['code'] = 200
                data['price'] = price
            else:
                data['code'] = 100

            return JsonResponse(data)


# 改变地址状态
def change_address_status(request):
    if request.method == "POST":
        user = request.user
        if user.id:
            id = request.POST.get('id')
            all_addresss = Address.objects.all()
            addresss = Address.objects.filter(user=user, id=id).first()
            if addresss:
                for addr in all_addresss:
                    addr.is_select = False
                    addr.save()
                addresss.is_select = True
                addresss.save()

                return JsonResponse({'code': 200})


# 删除地址
def remove_address(request):
    if request.method == 'POST':
        user = request.user
        if user.id:
            id = request.POST.get('id')
            address = Address.objects.filter(user=user, id=id).first()
            address.delete()
            return JsonResponse({'code': 200})


# 立即购买
def buy_now(request):
    if request.method == 'POST':
        user = request.user
        data = {}
        if user.id:
            g_id = request.POST.get('g_id')
            cart = Cart.objects.filter(user=user, goods_id=g_id).first()
            if cart:
                cart.c_num += 1
                cart.save()
                data['code'] = 200
            else:
                Cart.objects.create(user=user, goods_id=g_id)
                data['code'] = 200
            return JsonResponse(data)


# 提交订单
def submit_order(reuqest):
    if reuqest.method == 'POST':
        user = reuqest.user
        carts = Cart.objects.filter(user=user, is_select=True)
        o_num = get_order_num()
        order = Order.objects.create(user=user, o_num=o_num)
        for cart in carts:
            OrderGoods.objects.create(order=order, goods=cart.goods, goods_num=cart.c_num)
        carts.delete()
        return JsonResponse({'code': 200})


def o_price(request):
    if request.method == 'GET':
        o_id = request.GET.get('o_id')
        ogs = OrderGoods.objects.filter(order_id=o_id)
        prices = 0
        for og in ogs:
            prices += og.goods.price * og.goods_num
        prices = '%.2f' % prices
        return JsonResponse({'code': 200, 'prices': prices})
