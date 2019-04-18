from django.shortcuts import render


def cutter_list(request):
    return render(request, 'cutters/cutter_list.html', {})
    
