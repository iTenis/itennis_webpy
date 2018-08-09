from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
import json
import re
import uuid
from hashlib import sha1
from django.db import transaction
from .models import *
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import random
from utils.preset import preset_json, preset_str
from utils.proencrypt import proencrypt
from utils.islogin import islogin
from utils.senderror import decorator_error_monitor
from utils.sendmail import send_email
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger("sourceDns.webdns.views")


def Get_VaildCode_Img(request):
    # 随机创建图片
    img = Image.new(mode="RGB", size=(120, 40),
                    color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    draw = ImageDraw.Draw(img, "RGB")
    # 画干扰线
    for i in range(5):
        x1 = random.randint(0, 120)
        y1 = random.randint(0, 40)
        x2 = random.randint(0, 120)
        y2 = random.randint(0, 40)

        draw.line((x1, y1, x2, y2), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    font = ImageFont.truetype("static/fonts/KumoFont.ttf", 20)  # 20表示20像素

    str_list = []  # 吧每次生成的验证码保存起来
    # 随机生成五个字符
    for i in range(5):
        random_num = str(random.randint(0, 9))  # 随机数字
        random_lower = chr(random.randint(65, 90))  # 随机小写字母
        random_upper = chr(random.randint(97, 122))  # 随机大写字母
        random_char = random.choice([random_num, random_lower, random_upper])
        # print(random_char, "random_char")
        str_list.append(random_char)
        # (5 + i * 24, 10)表示坐标，字体的位置
        draw.text((5 + i * 24, 10), random_char,
                  (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), font=font)
    # print(str_list, "str_list")
    f = BytesIO()  # 内存文件句柄
    img.save(f, "png")  # img是一个对象
    data = f.getvalue()  # 读取数据并返回至HTML
    valid_str = "".join(str_list)
    logger.info("验证码为:"+str(valid_str))
    request.session["keep_valid_code"] = valid_str  # 把保存到列表的东西存放至session中
    return HttpResponse(data)

def SendMail(request):
    response = HttpResponse()
    try:
        str_list = []
        for i in range(5):
            random_num = str(random.randint(0, 9))
            str_list.append(random_num)
        valid_str = "".join(str_list)
        request.session["keep_mail_code"] = valid_str
        send_email(request.GET['maillist'],valid_str)
        context = preset_str(title='iTennis | 重置密码', page_cate=3, reurl='/apc/login/3', status_code='20000')
        response.write(json.dumps(context))
        return response
    except Exception as e:
        context = preset_str(title='iTennis | 重置密码', page_cate=3, reurl='/apc/login/3', status_code='40003')
        response.write(json.dumps(context))
        logger.error(str(e))
        return response


@csrf_exempt
def Login(request):
    response = HttpResponse()
    try:
        if request.method == 'GET':
            uid = request.COOKIES.get('uid', '')
            if uid != '':
                userinfo = UserInfo.objects.filter(id=uid)
                if len(userinfo) is 0:
                    context = preset_str(title='iTennis | 用户登录', page_cate=2, status_code='20007')  # 20007 用户名或者密码错误
                    response.write(json.dumps(context))
                    return response
                request.session['uid'] = userinfo[0].id
                request.session['ufullname'] = userinfo[0].ufullname
                request.session['uphoto'] = userinfo[0].uphoto
                context = preset_str(title='iTennis | 用户登录', page_cate=2, status_code='20000')  # 验证成功
                response.write(json.dumps(context))
                return response
            else:
                context = preset_str(title='iTennis | 用户登录', page_cate=2, reurl='apc/login.html', status_code='20008')
                response.write(json.dumps(context))
                return response
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            vialdcode = request.POST.get('vialdcode')
            remember = request.POST.get('remember', 0)
            title = 'iTennis | 用户登录'
            if username is '':
                status_code = '20003'  # 20003 用户名为空
                return preset_json(title=title, status_code=status_code)

            if vialdcode.lower() != request.session.get("keep_valid_code").lower():
                context = preset_str(title='  | 用户登录', page_cate=2, status_code='20009')
                response.write(json.dumps(context))
                return response

            if username is None or password is None:
                context = preset_str(title='  | 用户登录', page_cate=2, status_code='20034')
                response.write(json.dumps(context))
                return response

            logger.info('测试打印 username:' + username)
            logger.info('测试打印 password:' + password)
            logger.info('测试打印 vialdcode:' + str(vialdcode))
            logger.info('测试打印 remember:' + str(remember))

            user = UserCheck.objects.filter(uname=username, upwd=proencrypt(password))
            # user = UserCheck.objects.filter(uname=username, upwd=password)
            if len(user) is 0:
                context = preset_str(title='iTennis | 用户登录', page_cate=2, status_code='20007')
                response.write(json.dumps(context))
                return response
            else:
                userinfo = UserInfo.objects.filter(ucheckid=user[0].id)
                reurl = request.COOKIES.get('url', '/')
                if remember != 0:
                    response.set_cookie('uid', userinfo[0].id, max_age=30 * 24 * 3600)
                else:
                    response.set_cookie('uid', userinfo[0].id, max_age=60 * 60 * 12)
                request.session['uid'] = userinfo[0].id
                request.session['ufullname'] = userinfo[0].ufullname
                request.session['uphoto'] = userinfo[0].uphoto
                logger.info('测试Session:' + request.session.get('uid'))
                logger.info('测试Cookie:' + request.COOKIES.get('uid', ''))
                context = preset_str(title='iTennis | 用户登录', page_cate=2, reurl=reurl, status_code='20000')
                response.write(json.dumps(context))
                return response
    except Exception as e:
        logger.error("异常打印:" + str(e))
        context = preset_str(title='iTennis | 用户登录', page_cate=2, status_code='50001')
        response.write(json.dumps(context))
        return response


def Register(request):
    response = HttpResponse()
    try:
        if request.method == 'GET':
            context = preset_str(title='iTennis | 用户注册', page_cate=1, reurl='/apc/login/1', status_code='20000')
            response.write(json.dumps(context))
            return response
        else:
            post = request.POST
            title = 'iTennis | 用户注册'
            fullname = post.get('fullname')
            email = post.get('email')
            username = post.get('username')
            password = post.get('password')
            rpassword = post.get('rpassword')
            logger.info('测试打印 fullname:' + fullname)
            logger.info('测试打印 email:' + email)
            logger.info('测试打印 username:' + username)
            if fullname is '' or fullname is None:
                status_code = '20001'  # 20001 昵称为空
                return preset_json(title=title, status_code=status_code)
            if email is '' or email is None:
                status_code = '20002'  # 20002 邮箱为空
                return preset_json(title=title, status_code=status_code)
            if username is '' or username is None:
                status_code = '20003'  # 20003 用户名为空
                return preset_json(title=title, status_code=status_code)
            if password is '' or password is None:
                status_code = '20004'  # 20004 密码为空
                return preset_json(title=title, status_code=status_code)
            if rpassword is '' or rpassword is None:
                status_code = '20005'  # 20005 确认密码为空
                return preset_json(title=title, status_code=status_code)

            if password != rpassword:
                status_code = '20006'  # 20006 密码不一致
                return preset_json(title=title, status_code=status_code)
            logger.info("测试打印:用户信息插入数据库")
            with transaction.atomic():
                # 保存用户登录信息
                upwd = proencrypt(password)
                usercheck = UserCheck()
                userrole = UserRoles.objects.filter(rolename='普通用户')
                usercheck.id = str(uuid.uuid4()).replace('-', '')
                usercheck.uname = username
                usercheck.upwd = upwd
                usercheck.uroleid = userrole[0]
                usercheck.delflag = '0'  # 0:表示未删, 1:表示删除
                usercheck.save()

                # 保存用户的个人信息资料
                userinfo = UserInfo()
                statusflag = StatusFlag.objects.filter(sfname='正常')
                userinfo.id = str(uuid.uuid4()).replace('-', '')
                userinfo.uphoto = 'avatar3.jpg'
                userinfo.umail = email
                userinfo.ufullname = fullname
                userinfo.ucheckid = usercheck
                userinfo.ustatusid = statusflag[0]
                userinfo.save()
                return preset_json(title='iTennis | 用户注册', page_cate=1, status_code='20000')
    except Exception as e:
        logger.error("异常打印:" + str(e))
        return preset_json(title='iTennis | 用户注册', page_cate=1, status_code='50001')


def Forget(request):
    response = HttpResponse()
    try:
        if request.method == 'GET':
            context = preset_str(title='iTennis | 重置密码', page_cate=3, reurl='/apc/login/3', status_code='20000')
            response.write(json.dumps(context))
            return response
        else:
            # username = request.POST.get('fusername')
            email = request.POST.get('email')
            fcode = request.POST.get('fcode')
            newpassword = request.POST.get('newpassword')
            title = 'iTennis | 重置密码'
            if email is '':
                status_code = '20002'
                return preset_json(title=title, status_code=status_code)
            if fcode is '':
                status_code = '20009'
                return preset_json(title=title, status_code=status_code)
            if newpassword is '':
                status_code = '20004'
                return preset_json(title=title, status_code=status_code)

            # qnewpassword = request.POST.get('qnewpassword')
            if request.session.get("keep_mail_code") != fcode:
                context = preset_str(title='iTennis | 重置密码', page_cate=3, reurl='/apc/login/3', status_code='20009')
                response.write(json.dumps(context))
                return response
            UserCheck.objects.filter(uname=email).update(upwd=proencrypt(newpassword))
            context = preset_str(title='iTennis | 重置密码', page_cate=3, reurl='/apc/login/3', status_code='20000')
            response.write(json.dumps(context))
            return response
    except Exception as e:
        logger.error("异常打印:" + str(e))
        return preset_json(title='iTennis | 重置密码', page_cate=3, status_code='50001')


def CheckUser(request,user):
    response = HttpResponse()
    try:
        user = UserCheck.objects.filter(uname=user)
        if len(user) == 1:
            context = preset_str(title='iTennis | 用户注册', page_cate=1, reurl='/apc/login/1', status_code='20010')
            response.write(json.dumps(context))
            return response
        context = preset_str(title='iTennis | 用户注册', page_cate=1, reurl='/apc/login/1', status_code='20000')
        response.write(json.dumps(context))
        return response
    except Exception as e:
        logger.error("异常打印:" + str(e))
        context = preset_str(title='iTennis | 用户注册', page_cate=1, reurl='/apc/login/1', status_code='50001')
        response.write(json.dumps(context))
        return response




def Logout(request):
    request.session.flush()  # 键和值一起清空
    response = HttpResponseRedirect('/apc/login/2')
    response.delete_cookie('uid')
    return response


@islogin
def test(request):
    print(request.COOKIES)
    return HttpResponse(request.COOKIES)
