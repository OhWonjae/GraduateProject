from django.contrib import admin
from .models import UserInfo
from .models import MaskInfo
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(UserInfo)

@admin.register(MaskInfo)
class MaskInfo(admin.ModelAdmin):
    list_filter = ("date",)
