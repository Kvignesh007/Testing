from django.shortcuts import render, HttpResponse, redirect
from .models import register

# Create your views here.
def registerpage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = register()
        users.Name = name
        users.Address = address
        users.Username = username
        users.Password = password
        users.save()
    return render(request, 'registerpage.html')

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'admin@007':
            return HttpResponse('Welcome Admin')
        else:
            return HttpResponse('Invalid')
    return render(request,'adminlogin.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            register.objects.gets(Username=username,Password=password)
            return HttpResponse('Welcome User')
        except:
             return HttpResponse('Invalid User')
    return render(request,'userlogin.html')

