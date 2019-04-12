from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import *
from .models import ResourceForProduct,ResourceForModule

@require_GET
@csrf_exempt
def insertproduct(request):
    # 查询ResourceForProduct数据模型中的所有数据
    product_list=ResourceForProduct.objects.all()
    return render(request,'test_models.html',locals())

@require_POST
@csrf_exempt
def addproduct(request):
    product=ResourceForProduct()
    product.product_name="aap端"
    product.description="代表app端的产品"
    product.save( )
    return HttpResponse("添加产品成功")