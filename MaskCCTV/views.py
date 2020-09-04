from django.shortcuts import render
from .models import UserInfo
from .models import  MaskInfo
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
def cctvlogin(request):
    print(request.user.is_authenticated)
    if(request.user.is_authenticated):
        num_NamChuncheon = MaskInfo.objects.filter(adress = 'namchuncheon').count()
        num_MaskNamChuncheon = MaskInfo.objects.filter(adress = 'namchuncheon',set_mask=True).count()
        num_Gangnam = MaskInfo.objects.filter(adress = 'gangnam').count()
        num_MaskGangnam = MaskInfo.objects.filter(adress = 'gangnam',set_mask=True).count()
        num_Sareung = MaskInfo.objects.filter(adress = 'sareung').count()
        num_MaskSareung = MaskInfo.objects.filter(adress = 'sareung',set_mask=True).count()
        context = {
        'num_NamChuncheon' : num_NamChuncheon,
        'num_MaskNamChuncheon' : num_MaskNamChuncheon,
        'num_Gangnam' : num_Gangnam,
        'num_MaskGangnam' : num_MaskGangnam,
        'num_Sareung' : num_Sareung,
        'num_MaskSareung' : num_MaskSareung,
        'NamChuncheonRatio' : num_MaskNamChuncheon/num_NamChuncheon,
        'GangnamRatio' : num_MaskGangnam/num_Gangnam,
        'SareungRatio' :num_MaskSareung/num_Sareung,
        }
        print(num_MaskNamChuncheon/num_NamChuncheon)
        print(num_MaskGangnam/num_Gangnam)
        return render(request, 'MaskCCTV/CCTVhtml.html',context= context)
    else:
        return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return

def get(request,place,isMask):
    if(place=='namchuncheon' or place=='gangnam' or place=='sareung'):
        num_NamChuncheon = MaskInfo.objects.filter(adress = 'namchuncheon').count()
        num_MaskNamChuncheon = MaskInfo.objects.filter(adress = 'namchuncheon',set_mask=True).count()
        num_Gangnam = MaskInfo.objects.filter(adress = 'gangnam').count()
        num_MaskGangnam = MaskInfo.objects.filter(adress = 'gangnam',set_mask=True).count()
        num_Sareung = MaskInfo.objects.filter(adress = 'sareung').count()
        num_MaskSareung = MaskInfo.objects.filter(adress = 'sareung',set_mask=True).count()
        context = {
        'num_NamChuncheon' : num_NamChuncheon,
        'num_MaskNamChuncheon' : num_MaskNamChuncheon,
        'num_Gangnam' : num_Gangnam,
        'num_MaskGangnam' : num_MaskGangnam,
        'num_Sareung' : num_Sareung,
        'num_MaskSareung' : num_MaskSareung,
        'NamChuncheonRatio' : num_MaskNamChuncheon/num_NamChuncheon,
        'GangnamRatio' : num_MaskGangnam/num_Gangnam,
        'SareungRatio' :num_MaskSareung/num_Sareung,
        }
        if(isMask ==0):
            data = MaskInfo.objects.create(adress=place,set_mask = False)
            return render(request,'MaskCCTV/CCTVhtml.html',context=context)
        elif(isMask==1):
            data = MaskInfo.objects.create(adress=place,set_mask = True)
            return render(request,'MaskCCTV/CCTVhtml.html',context=context)