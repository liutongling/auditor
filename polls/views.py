from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Auditor
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request):
    template = loader.get_template("polls/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    result = "Fail"
    if username and password:
        user = Auditor.objects.filter(auditorName=username) # 根据名字找到用户
        if user: #如果用户存在，则进入判断
            # print(type(user[0].Academypassword)) 查看数据类型
            if user[0].Academypassword == int(password):
                result = "success"
                return render(request, 'polls/work.html', locals())
            else:
                return render(request, 'polls/g.html', locals())
        else:
            return render(request, 'polls/work.html', locals())
    return render(request, 'polls/g.html', locals())

def registeridx(request):
    template = loader.get_template("polls/register.html")
    context = {}
    return HttpResponse(template.render(context, request))

def register(request):
    username = request.POST.get('username')
    userUnit = request.POST.get('userUnit')
    password = request.POST.get('password')
    result = "Fail"
    confirmPassword = request.POST.get('confirmPassword')
    if confirmPassword == password:

        user = Auditor(auditorName=username, Academypassword=int(password),auditorUnit=userUnit)
        user.save()
        result = "Success"
        return render(request, 'polls/g.html', locals())
    return render(request, 'polls/g.html', locals())


def g(request):
    if request.method == 'GET':
        g = request.GET.get('g')
        return render(request, 'polls/g.html', locals())
    else:
        return HttpResponse('<UNK>')