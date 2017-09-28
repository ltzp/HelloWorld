#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2017/9/19 下午4:34
# @Author  : Letao@zingfront.com
# @Site    : 
# @File    : view.py
# @Software: SocialPeta

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from HelloWorld.unit.coreCode import Launge

def hello(request):
    context = {}
    context['hello'] = 'hello world'
    return render(request, 'hello.html', context)

@csrf_exempt
def getkey(request):
    content = request.POST.get("content").strip()
    result = Launge.statistics(content)
    return JsonResponse(json.dumps(result.encode('utf-8')), safe = False)


def getAPI(request):
    content = request.GET.get("content").strip()
    result = Launge.statistics(content)
    return JsonResponse(json.dumps(result.encode('utf-8')), safe = False)