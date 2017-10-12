from django.conf.urls import url, include
from rest_framework import routers, viewsets
from rest_framework.authtoken import views
from .serializers import ProductSerializer
from . import views


# ------- 3 --------
router = routers.DefaultRouter()
router.register(r'product', views.CreateListRetrieveViewSet, base_name='product')


urlpatterns = [
    # ------- 1 ------
    # url(r'^product', views.ProductList.as_view()),
    # ----------------

    # ------- 2 ------
    # url(r'^product_create', views.ProductModelViewSet.as_view({'post': 'create'})),
    # url(r'^product_list', views.ProductModelViewSet.as_view({'get': 'list'})),
    # url(r'^product_details/(?P<pk>\d+)', views.ProductModelViewSet.as_view({'get': 'retrieve'})),
    # ----------------

    # ------- 3 ------
    url(r'^', include(router.urls)),
    # ----------------



    url(r'^api-token-auth/', views.ObtainAuthToken.as_view()),
]