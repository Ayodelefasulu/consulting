from django.urls import path
from . import views

app_name = 'business'

urlpatterns = [
    path('', views.business_list, name='business_list'),
    #path('home/', views.home, name='home'),
    path('<int:id>', views.business_detail, name='business_detail'),
]
