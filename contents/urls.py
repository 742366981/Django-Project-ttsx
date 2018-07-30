from django.conf.urls import url

from contents import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^detail/(?P<tid>\d+)/(?P<gid>\d+)/', views.detail, name='detail'),
    url(r'^listre/',views.listre),
    url(r'^list/(?P<tid>\d+)/(?P<sid>\d+)/', views.list, name='list'),
    url(r'^placeOrder/', views.place_order, name='placeOrder'),
    url(r'^userCenterInfo/', views.user_center_info, name='userCenterInfo'),
    url(r'^userCenterOrder/', views.user_center_order, name='userCenterOrder'),
    url(r'^userCenterSite/', views.user_center_site, name='userCenterSite'),
]
