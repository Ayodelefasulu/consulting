from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
#from business.models import Business
#from public.models import Public
#from academics.models import Academic

# Create your views here.
def home(request):
    #return HttpResponse("This is Home!")
    return render(request, 'pages/index.html')
