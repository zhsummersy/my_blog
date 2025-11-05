"""djpsk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from blog import views as blog_views
from django.views.static import serve 
from djpsk import views

handler404 = views.page_not_found_error
handler500 = views.page_error

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('zhsummersy/', admin.site.urls),
    path('blog/', include('blog.urls')),
    #path('', include('home.urls')),
    path('home/',show_home_page),
    path('',show_home_page),
    path('about/',about),
    
    
    path('contact',contact),    
   # path('çategory/<int:cid>',show_category_page),

    path('search/',search),
    path('register/',blog_views.register,name='register'),
    path('profile/',blog_views.profile,name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='blog/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='blog/logout.html'),name='logout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='blog/password_reset.html'),name='password_reset'),
    path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name='blog/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='blog/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='blog/password_reset_complete.html'),name='password_reset_complete'),
    re_path('media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path('static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    
]
# +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
