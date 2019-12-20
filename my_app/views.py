import json

from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def my_api(request):
    dic = {}
    if request.method == 'GET':
        dic['message'] = 0
        return HttpResponse(json.dumps(dic))
    else:
        dic['message'] = '方法错误'
        return HttpResponse(json.dumps(dic, ensure_ascii=False))


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        return HttpResponse(username)
    else:
        return render_to_response('login.html')
