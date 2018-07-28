from django.conf.urls import url, include
from django.contrib.staticfiles.urls import static

from contents import views
from ttsx import settings

urlpatterns = [
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^contents/', include('contents.urls', namespace='contents')),
    url(r'^$', views.index),
    # url(r'^admin/', include('adminpractice.urls', namespace='admin')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
