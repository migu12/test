from django.shortcuts import render,HttpResponse

def runoob(request):
    views_list = ["菜鸟教程","菜鸟教程1","菜鸟教程2","菜鸟教程3",]
    return render(request, "runoob.html")
def login(request):
    return render(request, "User/login.html")
def index(request):
    return render(request, "index.html")
def draft(request):
    return render(request, "draft.html")
def border(request):
    return render(request, "border.html")
def test(request):
    return render(request, "test.html")
def liushuideng(request):
    return render(request, "liushuideng.html")
def img(request):
    return render(request, "img.html")
def button(request):
    return render(request, "button.html")
def text(request):
    return render(request, "text.html")
def register(request):
    return render(request, "User/register.html")