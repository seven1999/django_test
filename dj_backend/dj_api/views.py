# coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import models
from django import http
import logging

# Create your views here.

logger = logging.getLogger("django")


@csrf_exempt
def hello(req):
    print "============================", req.method
    print "============================", req.body
    print "============================", req.path
    # print "req.scheme============================", req.scheme
    print "path_info============================", req.path_info
    print "encoding============================", req.encoding
    print "COOKIES============================", req.COOKIES
    print "get_host============================", req.get_host()
    print "get_full_path============================", req.get_full_path()
    results = {
        "message": "success",
        "retcode": 0,
        "data": "hello world!~"
    }
    response = HttpResponse(json.dumps(results), status=200, content_type="application/json")
    return response


@csrf_exempt
def updateshop(request):
    result = {
        "message": "success",
        "retcode": 0,
        # "data": ""
    }
    data = json.loads(request.body)
    if request.method == "POST":
        shop_id = data.get('shopid', None).lower()
        name = data.get('name', None).lower()
        price = data.get('price', None).lower()
        description = data.get('description', None).lower()
        edit_shop = models.ShopTab.objects.get(shop_id=shop_id)
        edit_shop.name = name
        edit_shop.price = price
        edit_shop.description = description
        edit_shop.save()  # 把修改提交到数据库
    shop_id = request.GET.get("shop_id")
    # shop_obj = models.ShopTab.objects.get(shop_id=shop_id)  # 获取到数据内的这条记录，
    # result["data"] = shop_obj
    if not shop_id:
        result["message"] = "add fail"
        result["retcode"] = 500
    return get_api_response(result)


@csrf_exempt
def addshop(request):
    result = {
        "message": "success",
        "retcode": 0,
    }
    print request.method
    data = json.loads(request.body)
    print data
    if request.method == "POST":
        # shopid = request.POST.get("shopid", None)
        shop_id = data.get('shopid', None)
        country = data.get('country', None)
        item_id = data.get('itemid', None)
        name = data.get('name', None)
        price = data.get('price', None)
        stock = data.get('stock', 0)
        status = data.get('status', 1)
        description = data.get('description', None)
        models.ShopTab.objects.create(shop_id=shop_id, country=country, item_id=item_id, name=name, price=price,
                                      stock=stock, status=status, description=description)
    else:
        result["message"] = "add fail"
        result["retcode"] = 500
    return get_api_response(result)


@csrf_exempt
def delshop(request):
    result = {
        "message": "success",
        "retcode": 0,
    }
    data = json.loads(request.body)
    shopid = data.get('shopid').lower()
    if not shopid:
        result["message"] = "delete fail, pls check shopid"
        result["retcode"] = 500
    return get_api_response(result)


@csrf_exempt
def shopdetail(request):
    data = json.loads(request.body)
    shopid = data.get('shopid').lower()
    country = data.get('country').upper()
    result = get_buyer_detail(shopid=shopid, country=country)
    return get_api_response(result)


def get_buyer_detail(shopid, country='ID'):
    shop_infos = models.ShopTab.objects.filter(shop_id=shopid, country=country)
    if not shop_infos.exists():
        logger.info('not found any user info')
        return get_api_error(500, msg='shop info not found in ShopTab, shopid=%s, country=%s' % (shopid, country))

    shop_data = []
    for shop in shop_infos:
        shop_info = {
            'shop_id': shop.shop_id,
            'shop_name': shop.name,
            'status': shop.status,
            'item_id': shop.item_id
        }
        shop_data.append(shop_info)

    result = {
        "message": "success",
        "retcode": 0,
        "data": shop_data
    }
    return result


def get_api_response(data):
    return http.HttpResponse(json.dumps(data), content_type='application/json; charset=utf-8')


def get_api_error(code=0, remark=None, data=None, msg=''):
    if msg:
        message = msg
    else:
        message = ""

    ans = {
        'retcode': code,
        'message': message,
    }
    if remark:
        ans['remark'] = remark
    if data:
        ans['data'] = data
    return ans
