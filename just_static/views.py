from django.shortcuts import render # type: ignore
#from django.http import Http404, HttpResponse
#from business.models import Business
#from public.models import Public
#from academics.models import Academic

# Create your views here.
def home(request):
    #return HttpResponse("This is Home!")
    return render(request, 'pages/index.html')

def about(request):
    #return HttpResponse("This is About!")
    return render(request, 'pages/about.html')

def services(request):
    #return HttpResponse("This is Services!")
    return render(request, 'pages/services.html')