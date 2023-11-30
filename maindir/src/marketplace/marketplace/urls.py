from django.contrib import admin
from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^cart/', include('apps.cart.urls')),
    re_path(r'^', include('apps.market.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
