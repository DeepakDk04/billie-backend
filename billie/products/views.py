from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer


# Create your views here.


class ProductListView(ListAPIView):
    '''
    Displays all the Products
    '''
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]

    pagination_class = PageNumberPagination

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'category__name', 'code', 'category__code']
    ordering_fields = ['id', 'name', 'price', 'stockcount']

    ordering = ['-stockcount']


class ProductDetailView(RetrieveAPIView):
    '''
    Displays Single Product with Full Details
    '''
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'
