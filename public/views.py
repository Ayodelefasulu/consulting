from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Public

# Create your views here.
def public_list(request):
    public = Public.objects.all()
    return render(request, 'public/list.html', {'public': public})

def public_detail(request, id):
    public = get_object_or_404(Public, id=id, username = request.user)
    return render(request, 'public/detail.html', {'public': public})
