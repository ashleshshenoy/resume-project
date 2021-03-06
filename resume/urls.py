"""resume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from user import views as user_views
from main import views as main_views

urlpatterns = [
    path('', main_views.home, name="home-page"),
    path('signup/', user_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('admin/', admin.site.urls),
    path('about/', main_views.about, name='about'),
    path('resume/<str:username>/<str:resumeid>', main_views.preview, name='preview'), 
    path('resume-edit/', main_views.resume, name='resume'),
    path('video/edit/',main_views.video, name='video'), 
    path('video/delete/<int:id>', main_views.delete_video, name='delete-video'),
    path('profile', user_views.profile, name='profile'),
    path('profile/edit', user_views.profile_edit, name='profile-edit'),
    path('subscription',user_views.subscription_view, name='subscription'),

    

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
