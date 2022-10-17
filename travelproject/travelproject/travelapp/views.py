from django.http import HttpResponse
from django.shortcuts import render

from . models import Place
from . models import Travel
# Create your views here.



def demo(request):
    # name="india"
    obj=Place.objects.all()
    obj1=Travel.objects.all()



    return render(request,"index.html",{'result':obj ,'result1':obj1})





# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     mul=x*y
#     sub=x-y
#     div=x/y
#     return render(request, "result.html",{'add':add,'mul':mul,'sub':sub,'div':div})