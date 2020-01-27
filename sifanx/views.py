from django.shortcuts import render
from .models import index_img,testmony,feedback,gallery
from django.views.generic.edit import CreateView

# Create your views here.
def index (request):
    ur = testmony.objects.all().order_by('-id')
    te = index_img.objects.all()
    return render(request,'sifanx/index.html',{'ur':ur,'te':te})
    
def about (request):
    return render(request,'sifanx/about.html')
    
def services (request):
    return render(request,'sifanx/services.html')
    
def portfolio (request):
    p = gallery.objects.all().order_by('-id')
    return render(request,'sifanx/portfolio.html',{'p':p})
    
def thks (request):
    return render(request,'sifanx/test.html')
    
class testimonialCreate (CreateView):
    model = testmony
    fields = ['name','comment','images']
    
class feedbackCreate (CreateView):
    model = feedback
    fields = ['feedback']
    
def see_testimonial (request):
    see =testmony.objects.all().order_by('-id')
    return render(request,'sifanx/set.html',{'see':see})
    
    