from django.http import HttpResponse
from django.shortcuts import render




def hello(request):
    return HttpResponse("Hello world ! ")


def init(request):
    result = {'hello': '你好'}
    return render(request, 'init.html', result)

def login(request):
    return render(request, 'login.html')
