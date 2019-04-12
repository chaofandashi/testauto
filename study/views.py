from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

# 导入装饰器--请求部分
from django.views.decorators.http import *
# 逻辑处理模块，mtv中的v
# Create your views here.
# render用来往目标模板中传递一些内容
# 浏览器向服务器请求的对象，客户端发送过来的请求信息
# 模板的文件名index.html
# 对模板变量以及赋值
"""
render(request, template_name, context=None, content_type=None, status=None, using=None)
request HttpRequest 对象
template_name 模板名称-前端页面
context 页面展示的对象，模板中变量的赋值，dict类型
content_type 响应数据的数据格式
"""
# require_http_methods views 只接受特定的请求方法
# require_http_methods([get,post])可以接受get和post的请求:
# require_GET()
def index(request):
    info = {"title": "首页",'list':[1,5,"work"],"name":"hjp","ppp":"love"}
    return render(request, "index.html", info)

def index2(request):
    info = {
        "title": "我是第二页",
        "scheme": request.scheme,
        "body": request.body,
        "path": request.path_info,
        "method": request.method,
        "content_type": request.content_type,
        "encoding": request.encoding,
        "COOKIES": request.COOKIES,
        "GET": request.GET,
        "FILES": request.FILES,
    }
    return render(request, "second.html", info)

from django.http import QueryDict
# 请求数据被django转为QueryDict
# 导入queryDict 定义 QueryDict('a=1&a=2&b=3')
# 使用键创建一个新键iteration 每个值等于value
# get() 返回指定的值，不存在则返回none
# getlist 返回key所以有的值
# appedlist() 追加  pop copy clear
# dkct() 转化dict方法

# 导入csrf认证装饰器
from django.views.decorators.csrf import csrf_exempt


def input(reuqest):
    # name=reuqest.POST.get('name')
    return render(reuqest,"testform.html")
@csrf_exempt
def getName(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    return HttpResponse("你好，欢迎您%s。。。年龄%s" % (name,age))


from .forms import *
def myForm(request):
    forms_info = InfoForm()
    return render(request,'forms.html',locals())


def test(request):
    return render(request, 'test.html', locals())

def tempdemo(request):
    name='anges'
    info={'name':"anges","home":"shanghai","info":{"aaa":111,"bbb":222}}

    return render(request, 'base.html', locals())



























