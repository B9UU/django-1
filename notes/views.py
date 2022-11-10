from django.shortcuts import render
from django.http import Http404

from .models import Notes
# Create your views here.

def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/list.html', {'data':all_notes})

def details(request, pk):
    try:
        data = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404('Note Does"t exist')
    return render(request, 'notes/details.html',{'note':data})
