"""hotshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
from django.views.static import serve

import xadmin
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from goods.views import GoodsListView
from hotshop.settings import MEDIA_ROOT
from users.views import SmsCodeViewset, UserViewset,UserDetViewset
from user_operation.views import LeavingMessageViewset,AddressViewset

router = DefaultRouter()
# 配置url

router.register(r'user/getVerCode',SmsCodeViewset,base_name="user/getVerCode")
router.register(r'user/loginVerCode', UserViewset, base_name="user/loginVerCode")
router.register(r'mine/getUserInfo', UserDetViewset, base_name="mine/getUserInfo")

# 评价
router.register(r'shop/evaluate',LeavingMessageViewset,base_name="shop/evaluate")
router.register(r'address',AddressViewset,base_name="address")

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'docs/',include_docs_urls(title="tchg")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # 注册router
    url(r'^',include(router.urls)),

    # 商品列表展示
    url(r'goods/$',GoodsListView.as_view(),name = "goods-list"),
    # jwt认证登录接口
    url(r'^user/loginPwd', obtain_jwt_token),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),


]
