from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Auditor, Academy


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request):
    template = loader.get_template("polls/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

# 查询当前审核人员管理学院
def findAcademy(username):
    return Academy.objects.filter(auditorName=username)

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
                userUnit = user[0].auditorUnit
                # 将登录信息保存到session中
                request.session['username'] = username
                request.session['userUnit'] = userUnit
                latest_question_list = findAcademy(user[0].id)
                acad = Academy.objects.filter(auditorName_id=None)
                #从数据中获取审核的学院数
                question_len = len(latest_question_list)
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
# 这个函数是将通过前端添加学院将学院加入到审核人员
def AcademyAdd(request):
    print("come in")
    username = 'no username'
    if True:
        academyName = request.POST.get('academyId1')
        print(academyName)
        print("*****")
        username = request.session.get('username', 'no')# 将登录信息保存到session中
        addAuditor = Auditor.objects.filter(auditorName=username)
        Academy.objects.filter(Academyname=academyName).update(auditorName=addAuditor[0])
        #Academy(Academyname=academyName,auditorName=addAuditor[0],responsible1=responsible,responsibleTel=responsibleTel).save()
        print(username)
        return render(request, 'polls/g.html', locals())
    else:
        return render(request, 'polls/g.html', locals())
def delete(request):
    if request.method == 'POST':
        g = request.POST.get('academyId')

        s = Academy.objects.filter(Academyname=g).update(auditorName_id=None)

        print(s)
        return render(request, 'polls/g.html', locals())
    else:
        return HttpResponse('<UNK>')
def g(request):
    if request.method == 'GET':
        g = request.GET.get('g')
        return render(request, 'polls/g.html', locals())
    else:
        return HttpResponse('<UNK>')

def view(request):
    # 通过session获取当前的登录信息
    username = request.session.get('username', 'no')
    userUnit = request.session.get('userUnit')
    # 这里实现了一个需求，就是通过点击一个div方块，需要将该div方块的数据传递到下一个页面中，实现这个需要使用一个get请求，传递到下一个页面
    acad = request.GET.get('acad')
    Au = request.GET.get('acadA')
    ph = request.GET.get('Ph')
    print("*******")
    print(Au)
    print("*******")
    return render(request, 'polls/view.html', locals())


# 像数据库里面添加审核成员
def addP(request):
    return render(request,'polls/addPerson.html',locals())