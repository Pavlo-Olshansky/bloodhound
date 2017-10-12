from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import parsers,renderers, authentication, mixins
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework import routers, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductSerializer
from bloodhound.core.models import Product


# ---------------------------------- 1 --------------------------------
class ProductList(generics.ListAPIView):
	authentication_classes = (authentication.TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
# ---------------------------------------------------------------------

# ---------------------------------- 2 --------------------------------
class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
# ---------------------------------------------------------------------

# ---------------------------------- 3 --------------------------------
class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
# ---------------------------------------------------------------------


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)

        return Response({'Authorization Token': token.key})