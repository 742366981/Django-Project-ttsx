from django.conf.urls import url

from contents import views

urlpatterns = [
    # 首页
    url(r'^index/', views.index, name='index'),
    # 购物车
    url(r'^cart/', views.cart, name='cart'),
    # 添加商品
    url(r'^addCart/', views.add_cart),
    # 减少商品
    url(r'^reduceCart/', views.reduce_cart),
    # 获得购物车商品信息
    url(r'^getPrice/', views.get_price),
    # 获得详情页商品价格
    url(r'^getAPrice/', views.get_a_price),
    # 改变购物车商品状态
    url(r'^changeStatus/', views.change_status),
    # 全选
    url(r'^allSelect/', views.all_status),
    # 删除
    url(r'^goodDelete/', views.good_delete),
    # 商品详情
    url(r'^detail/(?P<tid>\d+)/(?P<gid>\d+)/', views.detail, name='detail'),
    # 立即购买
    url(r'buyNow/',views.buy_now),
    # 跳转全部商品列表页
    url(r'^listre/',views.listre),
    # 分类商品列表
    url(r'^list/(?P<tid>\d+)/(?P<sid>\d+)/', views.list, name='list'),
    # 支付
    url(r'^placeOrder/', views.place_order, name='placeOrder'),
    # 改变地址状态
    url(r'^changeAddressStatus/', views.change_address_status),
    # 删除地址
    url(r'^removeAddress/', views.remove_address),
    # 个人信息
    url(r'^userCenterInfo/', views.user_center_info, name='userCenterInfo'),
    # 全部订单
    url(r'^userCenterOrder/', views.user_center_order, name='userCenterOrder'),
    # 收货地址
    url(r'^userCenterSite/', views.user_center_site, name='userCenterSite'),
    # 提交订单
    url(r'^submitOrder/', views.submit_order),
    # 点击查看订单价格
    url(r'^oPrice/', views.o_price),
]
