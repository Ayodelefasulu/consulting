from django.urls import path
from . import views

app_name = 'public'

urlpatterns = [
    path('', views.public_list, name='public_list'),
    path('<int:id>', views.public_detail, name='public_detail'),
]
