from django.conf.global_settings import FORM_RENDERER
from django.shortcuts import render, redirect
from win32ui import CreateButton

from .models import Hotel
from .forms import DisplayHotels

# Create your views here.

#def createlogin(request):  # View for creating a customer login
 #   if request.method == 'CREATE':
  #      form = FORM_RENDERER(createlogin(request))
   #     if form.is_valid():
    #        form.save()
     #       return redirect('success_url')

def home(request):  # View for hotel
    hotels=Hotel.objects.all()
    context={'hotels':hotels}
    return render (request, 'hotel_view.html', context)


#def login(request):
 #   hotels=Hotel.objects.all()
  #  context={'hotels':hotels}
   # return render (request, 'index.html', context)

#def hotel_view(request):
 #   if request.method == 'POST':
  #      form = DisplayHotels(request.POST)
   #     if form.is_valid():
    #        form.save()
     #       return redirect('success_url')
    #else:
     #   form = DisplayHotels()
    #return render(request, 'patient_entry.html', {'form': form})

