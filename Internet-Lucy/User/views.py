from django.shortcuts import render
from User.models import Users

from django.http import HttpResponse

# Create your views here.
def register(request):
    return render(request,'User/register.html')
def login(request):
    return render(request, "User/login.html")

def register(request):
    method = request.method # 请求方法
    if method == "GET":
        return render(request, "User/register.html")
    elif method == "POST":
        username = request.POST.get("username")
        res = Users.objects.filter(username=username)

        """验证用户名是否存在"""
        if res:
            html = "<div><h1>sorry,用户名已被注册，请尝试新的用户名</h1><div><a href='/User/register'>重新注册</a></div></div>"
            return HttpResponse(html)

        password = request.POST.get("password")
        repassword = request.POST.get("repassword")
        if(password!=repassword):
            html = "<div><h1>两次密码不相同</h1><div><a href='/User/register'>重新注册</a></div></div>"
            return HttpResponse(html)

        phone = request.POST.get("phone")

        """添加数据"""
        Users.objects.create(phone=phone, username=username, password=password)

        html = "<div><h1>恭喜，注册成功！</h1></div>"
        return HttpResponse(html)
    
def login(request):
    method = request.method
    if method == "GET":
        return render(request, "User/login.html")
    elif method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = Users.objects.get(username=username)
            if password == user.password:
                html = "<div><h1>恭喜！登录成功！</h1><div><a href='/index'>进入首页</a></div></div>"
            else:
                html = "<div><h1>sorry,密码错误，请重新输入密码</h1><div><a href='/user/login'>重新登录</a></div></div>"

            return HttpResponse(html)

        except user.models.User.DoesNotExist:
            html = "<div><h1>sorry,用户名不存在</h1><div><a href='/user/login'>重新登录</a></div></div>"
            return HttpResponse(html)
