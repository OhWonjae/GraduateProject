from django.shortcuts import render
from .models import UserInfo
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
def login(request):
    print(request)
    if request == "POST":
        userid = request.POST['userID']
        userpwd = request.POST['userPWD']
        print(userid + ' ' + userpwd)
        if userid=='admin' and userpwd=='admin':
            return render(request, 'MaskCCTV/CCTVhtml.html')
        else:
            return render(request, 'MaskCCTV/CCTVhtml.html', {'error': 'UserID or UserPassword is in correct'})
    else:
        return render(request,'MaskCCTV/login.html')
def logout(request):
    auth.logout(request)
    return