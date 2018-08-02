from random import randrange

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse

from contents.models import MainWheel, MainAdv, Goods, GoodsType, Cart


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


def cart(request):
    if request.method == 'GET':
        user = request.user
        if user.id:
            carts = Cart.objects.filter(user=user)
        return render(request, 'contents/cart.html', {'carts': carts})


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


def listre(request):
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('contents:list', kwargs={'tid': '1000', 'sid': 0}))


def list(request, tid, sid):
    if request.method == 'GET':
        # 随机选取2个推荐商品
        rgoods = Goods.objects.all()
        i = randrange(len(rgoods))
        rgoods = rgoods[i:i + 2]
        gts = GoodsType.objects.all()
        if tid == '1000':
            if sid == '0':
                goods = Goods.objects.all().order_by('name')
            if sid == '1':
                goods = Goods.objects.all().order_by('price')
            if sid == '2':
                goods = Goods.objects.all().order_by('-price')
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


def place_order(request):
    if request.method == 'GET':
        return render(request, 'contents/place_order.html')


def user_center_info(request):
    if request.method == 'GET':
        return render(request, 'contents/user_center_info.html')


def user_center_order(request):
    if request.method == 'GET':
        return render(request, 'contents/user_center_order.html')


def user_center_site(request):
    if request.method == 'GET':
        return render(request, 'contents/user_center_site.html')


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


def get_price(request):
    if request.method == 'GET':
        user = request.user
        if user.id:
            carts = Cart.objects.filter(user=user)
            prices=0
            counts=0
            for cart in carts:
                if cart.is_select:
                    prices+=cart.goods.price*cart.c_num
                    counts+=cart.c_num
            prices='%.2f'%prices
            return JsonResponse({'prices':prices,'counts':counts})


def change_status(request):
    if request.method=='POST':
        user=request.user
        data={}
        if user.id:
            g_id=request.POST.get('g_id')
            cart=Cart.objects.filter(user=user,goods_id=g_id).first()
            if cart.is_select:
                cart.is_select=False
                cart.save()
            else:
                cart.is_select=True
                cart.save()
            return JsonResponse({'code':200,'is_select':cart.is_select})


def all_status(request):
    if request.method=='POST':
        user=request.user
        if user.id:
            carts=Cart.objects.all()
            for cart in carts:
                cart.is_select=True
                cart.save()
            return JsonResponse({'code':200})


def good_delete(request):
    if request.method=='POST':
        user=request.user
        if user.id:
            g_id=request.POST.get('g_id')
            cart=Cart.objects.filter(user=user,goods_id=g_id).first()
            cart.delete()
            return JsonResponse({'code':200})
