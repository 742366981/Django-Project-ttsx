from datetime import datetime, timedelta

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from users.models import User,UserTicket
from utils.functions import get_ticket


def login(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pwd')
        if User.objects.filter(username=username).exists():
            user=User.objects.filter(username=username).first()
            if check_password(password,user.password):
                res=HttpResponseRedirect(reverse('contents:index'))
                out_time = datetime.now() + timedelta(days=1)
                ticket=get_ticket()
                res.set_cookie('ticket',ticket,expires=out_time)
                UserTicket.objects.create(user=user,ticket=ticket,out_time=out_time)
                return res
            else:
                return HttpResponseRedirect(reverse('users:login'))
        else:
            return HttpResponseRedirect(reverse('users:login'))




def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html')
    if request.method=='POST':
        username=request.POST.get('user_name')
        password=request.POST.get('pwd')
        cpassword=request.POST.get('cpwd')
        email=request.POST.get('email')
        if password==cpassword:
            password=make_password(password)
            User.objects.create(username=username,password=password,email=email)
            return HttpResponseRedirect(reverse('users:login'))


def logout(request):
    res=HttpResponseRedirect(reverse('contents:index'))
    res.delete_cookie('ticket')
    return res
