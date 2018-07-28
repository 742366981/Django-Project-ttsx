from random import randrange

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from contents.models import MainWheel, MainAdv, Goods, GoodsType


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
        return render(request, 'contents/cart.html')


def detail(request, tid, gid):
    if request.method == 'GET':
        gts=GoodsType.objects.all()
        # 随机选取2个推荐商品
        rgoods = Goods.objects.all()
        i = randrange(len(rgoods))
        rgoods = rgoods[i:i + 2]
        gt=GoodsType.objects.get(gt_id=tid)
        good = Goods.objects.filter(g_id=gid,gt=gt).first()
        return render(request, 'contents/detail.html', {'good': good, 'tid': tid,'gid':gid,'gts':gts,'rgoods':rgoods})


def listre(request):
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('contents:list', kwargs={'tid': '1000'}))


def list(request, tid):
    if request.method == 'GET':
        # 随机选取2个推荐商品
        rgoods=Goods.objects.all()
        i=randrange(len(rgoods))
        rgoods=rgoods[i:i+2]
        gts = GoodsType.objects.all()
        if tid == '1000':
            goods = Goods.objects.all()
        else:
            gtss=GoodsType.objects.get(gt_id=tid)
            goods = Goods.objects.filter(gt=gtss)

        return render(request, 'contents/list.html', {'tid': tid, 'gts': gts, 'goods': goods,'rgoods':rgoods})


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
