from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request):
    template = loader.get_template("polls/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
        if username == 'admin' and password == '1234567':
            return render(request, 'polls/g.html', locals())
    return render(request, 'polls/test', locals())

def registeridx(request):
    template = loader.get_template("polls/register.html")
    context = {}
    return HttpResponse(template.render(context, request))



def g(request):
    if request.method == 'GET':
        g = request.GET.get('g')
        return render(request, 'polls/g.html', locals())
    else:
        return HttpResponse('<UNK>')