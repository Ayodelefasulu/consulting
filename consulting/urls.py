"""
URL configuration for consulting project.

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
from django.contrib import admin # type: ignore
from django.urls import include, path # type: ignore
from . import views

urlpatterns = [
    #path('home/', views.home, namespace='home'),
    path('admin/', admin.site.urls),
    path('home/', include('just_static.urls', namespace='home')),
    path('about/', include('just_static.urls', namespace='about')),
    path('services/', include('just_static.urls', namespace='services')),
    path('faq/', include('just_static.urls', namespace='faq')),
    path('portfolio/', include('just_static.urls', namespace='portfolio')),
    path('public/', include('public.urls', namespace='public')),
    path('academics/', include('academics.urls', namespace='academics')),
    path('business/', include('business.urls', namespace='business')),
]
