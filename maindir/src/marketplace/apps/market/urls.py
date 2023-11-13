from django.urls import path, include
import api.views.market as view
urlpatterns = [
    path('', view.test()),

]
