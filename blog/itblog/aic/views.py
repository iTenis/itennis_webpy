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
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from aac.models import Articles, ArtcleCates, SaySomethings, UserOperate, OptTarget, OptType
from utils.page_next import page_obj


def Index(request):
    response = HttpResponse()
    try:
        objs = Articles.objects.all()
        context = page_obj(objs, request.GET.get('page', 1), 10)
        context['data']={'data1':objs[:3],'data2':objs[:4]}
        return render(request, 'aic/index.html', context)

    except Exception as e:
        print("异常打印:", e)
        context = preset_str(title='iTennis | 首页', status_code='40002')
        response.write(json.dumps(context))
        return response
