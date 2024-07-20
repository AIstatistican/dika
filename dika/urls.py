"""
URL configuration for dika project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from anasayfa.views import home_view, faysal_view,hakkinda_view, toplanti_view, amacimiz_view,yonetim_view, iletisim_view, bilimkurulu_view
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view, name='home'),
    path('post/', include('post.urls')),
    path('vlogs/', faysal_view, name='faysal view'),
    path('hakkinda/',hakkinda_view,name='hakkinda view'),
    path('toplanti/',toplanti_view,name='toplanti'),
    path('Amacimiz/', amacimiz_view,name='amacimiz view' ),
    path('iletisim/', iletisim_view, name='iletisim view'),
    path('accounts/', include('accounts.urls')),
    path('yonetim/', yonetim_view,name='yonetim view'),
    path('bilimkurulu/', bilimkurulu_view, name='bilim kurulu'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete')
]


