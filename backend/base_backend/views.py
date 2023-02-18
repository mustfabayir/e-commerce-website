from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.serializers import Serializer
from .models import *
from .serializers import *

@api_view(['GET'])
def get_products(request):
    query = request.query_params.get('keyword')
    products = Product.objects.filter(name__icontains=query).order_by('-_id')
    
    page = request.query_params.get('page')
    paginator = Paginator(products, 2)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    if page == None:
        page = 1
    page = int(page)

    seralizer = ProductSerializer(products, many=True)
    return Response({'products': seralizer.data, 'page': page, 'pages': paginator.num_pages})


@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

#Maybe get best products also

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_product(request):
    user = request.user
    product = Product.objects.create(
        user=user,
        price = 0,
        name = 'Sample name',
        in_stock_count = 0,
        brand = 'Sample brand',
        category = 'Sample category',
        description = '',
    )

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_product(request, pk):
    product = Product.objects.get(_id=pk)
    data = request.data

    product.name = data['name']
    product.price = data['price']
    product.in_stock_count = data['in_stock_count']
    product.category = data['category']
    product.description = data['description']
    product.brand = data['brand']

    product.save()

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_product(request, pk):
    product = Product.objects.get(_id = pk)
    product.delete()
    return Response('Product deleted')