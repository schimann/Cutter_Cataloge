from django.shortcuts import render
from .models import Cutter


def cutter_list(request):
    tools = Cutter.objects.filter(cutter_name__icontains = 'hog')
    return render(request, 'cutters/cutter_list.html', {'tools': tools})
