from django.contrib import admin
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^admin/', include(admin.site.urls)),
    re_path(r'^cart/', include('apps.cart.urls', namespace='cart')),
    re_path(r'^', include('apps.market.urls', namespace='shop')),
]