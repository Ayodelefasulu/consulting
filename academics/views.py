from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Academic

# Create your views here.
def academics_list(request):
    academics = Academic.objects.all()
    return render(request, 'academics/list.html', {'academics': academics})

def academics_detail(request, id):
    academics = get_object_or_404(Academic, id=id, username = request.user)
    return render(request, 'academics/detail.html', {'academics': academics})
