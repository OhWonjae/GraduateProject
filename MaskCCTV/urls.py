from django.urls import path
from MaskCCTV import views
urlpatterns = [
    path('',views.cctvlogin, name='cctvlogin'),

            ]

