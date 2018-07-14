from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models
# Create your views here.

user_list = []
def index(request):
    #return HttpResponse("hello Django!")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
       # temp = {"user": username, "pwd": password}
       # user_list.append(temp)
        #添加数据到数据库
        models.UserInfo.objects.create(user=username, pwd=password)
    user_list = models.UserInfo.objects.all()
    return render(request, "index.html", {"data": user_list})