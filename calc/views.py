from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def add(request):
    valu1=int(request.POST["num1"])
    valu2=int(request.POST["num2"])

    valu3=int(request.POST["num3"])
    valu4=int(request.POST["num4"])

    valu5=int(request.POST["num5"])
    valu6=int(request.POST["num6"])

    valu7=int(request.POST["num7"])
    valu8=int(request.POST["num8"])
    ares=valu1+valu2

    sres=valu3-valu4
    mres=valu5*valu6
    dres=valu7//valu8
    return render(request, 'result.html',{"result":ares ,"subresult":sres,"mres":mres ,"dres":dres})