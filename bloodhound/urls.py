from django.conf.urls import include, url
from django.contrib import admin
from bloodhound.core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.products_list, name='home'),
    url(r'^products/$', views.products_list, name='products'),
    url(r'^products/(\d+)/$', views.product_details, name='product'),
    url(r'^products/(\d+)/refresh/$', views.product_refresh, name='refresh'),
    url(r'^hot/$', views.hot, name='hot'),
    url(r'^api/', include('api.urls', namespace='api')),
]
