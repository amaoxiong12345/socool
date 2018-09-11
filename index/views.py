import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from index.forms import LoginForm
from index.models import *


def index_views(request):
    mes1 = '登录'
    url1 = '/login/'
    mes2 = '注册有惊喜'
    if 'uphone' in request.session and 'uid' in request.session:
        mes1 = '注销'
        url2 = '#'
        mes2 = '领取注册奖励'
    return render(request,'fruit.html',locals())

def login_views(request):
    if request.method == 'GET':
        if 'uphone' in request.session and 'uid' in request.session:
            return redirect('/')
        else:
            if 'uphone' in request.COOKIES and 'uid' in request.COOKIES:
                uphone = request.COOKIES['uphone']
                uid = request.COOKIES['uid']
                request.session['uphone'] = uphone
                request.session['uid'] = uid
                return redirect('/login/')
            else:
                form = LoginForm()
                return render(request,'login.html',locals())
    else:
        uphone = request.POST['numb']
        upwd = request.POST['passwd']
        user = Users.objects.filter(uphone=uphone, upwd=upwd, isActive=1)
        if user:
            request.session['uphone'] = uphone
            request.session['uid'] = user[0].id
            resp = redirect('/')
            if 'remeber' in request.POST:
                resp.set_cookie('uphone',uphone,60*60*24*14)
                resp.set_cookie('uid',user[0].id,60*60*24*14)
            return resp
        else:
            resp = '登录失败，请重新输入'
            return render(request, 'login.html', locals())


def register_views(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        uphone = request.POST['numb']
        upwd = request.POST['passwd']
        uname = request.POST['uname']
        uemail = request.POST['uemail']
        dic = {
            'uphone': uphone,
            'upwd': upwd,
            'uname': uname,
            'uemail': uemail,
            'isActive': 1
        }
        user = Users(**dic)
        user.save()
        return redirect('/login/')

# 检查手机号码是否存在
def server01_views(request):
    if request.method == 'POST':
        uphone = request.POST['uphone']
        uList = Users.objects.filter(uphone=uphone)
        if uList:
            # 手机号码存在，响应status 为0
            dic = {
                "staus":"0",
                "text":'手机号码已存在'
            }
            return HttpResponse(json.dumps(dic))
        else:
            dic = {
                "status":"1",
                "text":'可以注册'
            }
            return HttpResponse(json.dumps(dic))

def server02_views(request):
    pass

def server03_views(request):
    pass

def server04_views(request):
    pass

def checkLogin_views(request):
    if 'uid' in request.session and 'uphone' in request.session:
        uid = request.session["uid"]
        user = Users.objects.get(id=uid)
        dic = {
            "status":1,
            "txt":json.dumps(user.to_dict())
        }
        jsonStr = json.dumps(dic)
    else:
        if 'uid' in request.COOKIES and 'uphone' in request.COOKIES:
            uid = request.COOKIES['uid']
            uphone = request.COOKIES['uphone']
            request.session['uid'] = uid
            request.session['uphone'] = uphone
        else:
            dic = {
            "status":0,
            }
        jsonStr = json.dumps(dic)
    return HttpResponse(jsonStr)

def exit_views(request):
    url = request.META.get('HTTP_REFERER','/')
    resp = redirect(url)
    if 'uid' in request.COOKIES and 'uphone' in request.COOKIES:
        resp.delete_cookie('uid')
        resp.delete_cookie('uphone')
    if 'uid' in request.session and 'uphone' in request.session:
        del request.session['uid']
        del request.session['uphone']
    return resp

def loadGoods_views(request):
    goodstypes = GoodsType.objects.filter()
    all = []
    print(goodstypes)
    for goodstype in goodstypes:
        print(goodstype.title)
        l = []
        goods = Goods.objects.filter(goodsType=goodstype.id)
        for good in goods:
            d = good.to_dict()
            dtxt = json.dumps(d)
            l.append(dtxt)
        goodstxt = json.dumps(l[0:10])
        dic = goodstype.to_dict()
        dic['goods'] = goodstxt
        dictxt = json.dumps(dic)
        all.append(dictxt)
    jsonStr = json.dumps(all)
    return HttpResponse(jsonStr)

# 查询购物车内的商品数量
def cart_count_views(request):
    if 'uid' not in request.session:
        dic = {
            'count':0
        }
        return HttpResponse(json.dumps(dic))
    else:
        uid = request.session['uid']
        all_cart = CartInfo.objects.filter(users_id=uid)
        total_count = 0
        if  not all_cart:
            for cart in all_cart:
                total_count += cart.ccount
        dic={
            "count":total_count
        }
        return HttpResponse(json.dumps(dic))