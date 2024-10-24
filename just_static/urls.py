from django.urls import path # type: ignore
from . import views

app_name = 'just_static'

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.about, name='about'),
    path('', views.services, name='services'),
    #path('<int:id>', views.public_detail, name='public_detail'),
]
