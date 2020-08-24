from django.urls import path
from MaskCCTV import views
urlpatterns = [
    path('',views.login, name='login'),
    path('login/',views.login,name='maskcctv'),
    path('logout/',views.logout,name='logout'),

            ]

