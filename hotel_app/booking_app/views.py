from django.shortcuts import render
from .models import  Hotel

# Create your views here.
def home(request):
    hotels=Hotel.objects.all()
    context={'hotels':hotels}
    return render (request, 'hotel_view.html', context)
