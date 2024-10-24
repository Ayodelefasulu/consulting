from django.urls import path
from . import views

app_name = 'just_static'

urlpatterns = [
    path('', views.home, name='home'),
    #path('<int:id>', views.public_detail, name='public_detail'),
]
