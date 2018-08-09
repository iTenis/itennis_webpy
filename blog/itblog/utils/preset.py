#!/usr/bin/python
# -*- coding:utf-8 -*-
from django.http import JsonResponse
import json


def preset_json(title=None, keywords=None, description=None, data=None, page_cate=None,reurl =None,page_obj=None,page_list=None, page_id=None, page_size=None,
           status_code=None,
           *args, **kwargs):
    ret = {
        'title': title,  # 页面标题
        'keywords': keywords,  # 页面关键字
        'description': description,  # 页面描述信息
        'data': data,  # 传递页面数据
        'page_cate': page_cate,  # 页面类型
        'reurl': reurl, # 跳转页面
        'page_obj': page_obj, # 分页对象
        'page_list': page_list, # 分页序号列表
        'page_id': page_id,  # 页面id
        'page_size': page_size,  # 页面大小
        'status_code': status_code,  # 状态信息
    }
    result = json.dumps(ret)
    return JsonResponse(result, safe=False)

def preset_str(title=None, keywords=None, description=None, data=None, page_cate=None,reurl =None,page_obj=None,page_list=None, page_id=None, page_size=None,
           status_code=None,
           *args, **kwargs):
    ret = {
        'title': title,  # 页面标题
        'keywords': keywords,  # 页面关键字
        'description': description,  # 页面描述信息
        'data': data,  # 传递页面数据
        'page_cate': page_cate,  # 页面类型
        'reurl': reurl, # 跳转页面
        'page_obj': page_obj, # 分页对象
        'page_list': page_list, # 分页序号列表
        'page_id': page_id,  # 页面id
        'page_size': page_size,  # 页面大小
        'status_code': status_code,  # 状态信息
    }
    return ret