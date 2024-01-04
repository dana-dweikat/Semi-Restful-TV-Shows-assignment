from django.shortcuts import render,redirect

from .models import *
from .forms import ShowForm


def main(request):
    return redirect('app1:shows')

def shows(request):
    all_shows = Show.objects.all()
    
    context={
        'all_shows' : all_shows
    }
    
    return render(request, 'index.html', context)






def show(request, pk):
    show = Show.objects.get(id=pk)
    
    context={
        'show' : show
    }
    
    return render(request, 'display_show.html', context)


def add(request):
    
    form = ShowForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('app1:shows')
    
    context = {
        "form": form
    }
    
    return render(request, 'add_show.html', context)

def edit_show(request, pk):
    show = Show.objects.get(id=pk)
    form = ShowForm(request.POST or None, instance=show)
    
    if form.is_valid():
        form.save()
        return redirect('app1:shows')
    
    context = {
        "form": form,
        "show": show
    }
    
    return render(request, 'edit_show.html', context)


def delete_show(request, pk):
    show = Show.objects.get(id=pk)
    show.delete()
    return redirect('app1:shows')

