from django.urls import re_path
import api.views.market as views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$', views.product_list, name='product_list'),

    re_path(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),

    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
