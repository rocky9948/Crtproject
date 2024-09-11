"""
URL configuration for super project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from app.views import contact_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('eve1',views.ev1),
    path('login/',views.log),
    path('login/forget.html',views.forg),
    path('register/',views.reg),
    path('',views.mia),
    path('contact/',views.cont),
    path('Aboutus',views.abo),
    path('doregister/',views.doreg),
    path('logincheck/',views.logincheck),
    path('login/reset',views.rest),
    path('userhome/',views.use),
    path('adminhome/',views.adm),
    path('Viewusers/',views.vus),
    path('Viewcon/',views.con),
    path('modify/',views.modi),
    path('logout/',views.logout),
    path('login/getotp/',views.getotp),
    path('login/getotp/verifyotp/',views.verifyotp),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),  
     path('contact/', contact_view, name='contact'),
    
    
    
]

admin.site.site_header = "HAPPYEVENTS"
admin.site.site_title = "HAPPYEVENTS"
admin.site.index_title = "Welcome to HAPPYEVENTS"
