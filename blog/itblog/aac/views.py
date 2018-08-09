from django.shortcuts import render
from utils.islogin import islogin
from .models import *
from apc.models import UserInfo,UserCheck
from django.http import HttpResponse
from django.db import transaction
import logging
from utils.preset import preset_json, preset_str
from django.conf import settings
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator
import json
# Create your views here.
logger = logging.getLogger("sourceDns.webdns.views")
@islogin
#展示个人所有的文章说说
def ToListAllMine(request):
    uid = request.COOKIES.get('uid', '')
    # articleCount=articleList.count()
    context = {'title': 'iTennis | 我的发表','uid': uid, 'error_name': 'ok'}
    return render(request, 'aac/listallmine.html', context)

#富文本编辑器
def editor(request):
    return render(request, 'other/editor.html')

@islogin
def ToAddArticle(request):
    uid = request.COOKIES.get('uid', '')
    articlecates =ArtcleCates.objects.all()
    # print(articlecates[0])
    # print(articlecates[0].acatename)
    context = {'title': 'iTennis | 新增文章','articlecates':articlecates, 'error_name': 'ok'}
    return render(request, 'aac/addarticles.html', context)

def upload(request):
    if request.method == "POST":
        f1 = request.FILES['articlephoto']
        fname = '%s/cars/%s' % (settings.MEDIA_ROOT,f1.name)
        with open(fname, 'w') as articlephoto:
            for c in f1.chunks():
                articlephoto.write(c)
        return HttpResponse("ok")
    else:
        return HttpResponse("error")
# #新增文章
# def AddArticle(request):
#     response = HttpResponse()
#     try:
#         if request.method == 'GET':
#             print("!!!!!!!!!!!!!!!G")
#             return response
#         else:
#             print("1!!!!!!!!!!!!!!!!!!!P")
#             post = request.POST
#             articletitle = post.get('title')
#             content = post.get('content')
#             uid = post.get('uid')
#             print("11111111111111111111111111",uid)
#             title = 'iTennis | 用户注册'
#             logger.info('测试打印 fullname:' + articletitle)
#             logger.info('测试打印 email:' + content)
#             logger.info('测试打印 username:' + uid)
#             if articletitle is '' or articletitle is None:
#                 status_code = '30001'  # 20001 标题为空
#                 return preset_json(title=title, status_code=status_code)
#             if content is '' or content is None:
#                 status_code = '20002'  # 20002 文章内容为空
#                 return preset_json(title=title, status_code=status_code)
#             logger.info("测试打印:博客插入数据库")
#             articles = Articles()
#             with transaction.atomic():
#                 articles.uid = uid
#                 articles.posttittle = articletitle
#                 print("11111111111111111111111111", articles.posttittle)
#                 articles.saycontent = content
#                 articles.delflag = '0'
#                 postcate = ArtcleCates.objects.filter(acatename='生活')
#                 print("11111111111111111111111111",len(articles.postcate))
#                 articles.postcate = postcate[0]
#                 articles.save()
#                 return preset_json(title='iTennis | 用户注册', page_cate=1, status_code='20000')
#     except Exception as e:
#         logger.error("异常打印:" + str(e))
#         return preset_json(title='iTennis | 用户注册', page_cate=1, status_code='50001')