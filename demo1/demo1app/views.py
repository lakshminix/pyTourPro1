from django.http import HttpResponse
from django.shortcuts import render
from.models import Place
from.models import Team
# Create your views here.


# task1
# def home(request):
#     return HttpResponse("Hello ,this is home page")
# def about(request):
#     return render(request,'about.html')
# def contact(request):
#     return HttpResponse("Contact us :")
# def detail(request):
#     return render(request,'detail.html')
# def thankyou(request):
#     return HttpResponse("Thank You")

#task2

# def integer(request):
#     return render(request,'input.html')
#
# def operation(request):
#     x= int(request.GET['num1'])
#     y= int(request.GET['num2'])
#     add=x+y
#     mul=x*y
#     div=x/2
#     sub=x-y
#     return render(request,'result.html',{'addition':add,'multiplication':mul,'division':div,'subtraction':sub})

#task static

def demo(request):
    plc=Place.objects.all()
    tm=Team.objects.all()
    return render(request,'index.html',{'result1': plc,'result2': tm})