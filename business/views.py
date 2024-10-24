from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Business

# Create your views here.
def business_list(request):
    business = Business.objects.all()
    return render(request, 'business/list.html', {'business': business})

def business_detail(request, id):
    business = get_object_or_404(Business, id=id, username = request.user)
    return render(request, 'business/detail.html', {'business': business})
