from django.shortcuts import render
from .models import Immobile

def list_location(request):
    immobiles = Immobile.objects.filter(is_locate=False)
    context = {
        'immobiles': immobiles
    }

    return render(request, 'list-location.html', context)