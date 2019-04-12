"""testauto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# url的配置文件
from django.contrib import admin
from django.urls import path
# 导入view的index方法
from study import views,views_models
from study import urls
# 路由的集合列表  /是分隔符 必须添加
# view下面的index方法  前面的index是url的path
# view下面的index2方法  前面的org是url的path
# include导入的url文件没有配置任何一个url地址时，会在启动时报错
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('second/', views.index2),

    path('input/', views.input),
    path('getname/', views.getName),

    path('myforms/', views.myForm),

    path('test/', views.test),
    path('tempdemo/', views.tempdemo),

    path('mmm/',views_models.insertproduct),
    path('addproduct/',views_models.addproduct)
]
