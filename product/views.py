from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Product
from .serializers import ProductSerializer
from .filter import ProductsFilter

@api_view(['GET'])
def get_all_products(request):
    filterset = ProductsFilter(request.GET, queryset=Product.objects.all().order_by('id'))
    #مسئول عن عدد العناصر اللي هتظهر في الصفحة الواحدةpagination
    #لو هتشغلها حط queryset في serializer بدل filterset.qs
    #, "per page":resPage, "count":count
    # count = filterset.qs.count()
    # resPage = 2
    # paginator = PageNumberPagination()
    # paginator.page_size = resPage
    # queryset = paginator.paginate_queryset(filterset.qs, request)
    serializer = ProductSerializer(filterset.qs, many=True)
    return Response({"products":serializer.data})

@api_view(["GET"])
def get_by_id_product(request,pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response({"product":serializer.data})