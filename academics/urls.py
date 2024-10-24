from django.urls import path
from . import views

app_name = 'academics'

urlpatterns = [
    path('', views.academics_list, name='academics_list'),
    path('<int:id>', views.academics_detail, name='academics_detail'),
]
