from django.shortcuts import render, redirect
from .models import Network,Show
import datetime

def index(request):
    return redirect('/shows')

def shows(request):
    allshows = {
        "shows": Show.objects.all()
    }
    return render(request, 'shows.html',allshows)

def displayshow(request, show_id):
    oneshow = {
        "show": Show.objects.filter(id=show_id)
    }
    return render(request, 'show.html',oneshow)

def editshow(request, show_id):
    oneshow = {
        "show": Show.objects.filter(id=show_id)
    }
    return render(request, 'edit.html',oneshow)

def update(request, show_id):
    if request.method == "POST":
        showupdater = Show.objects.get(id=show_id)
        showupdater.title = request.POST['title']
        showupdater.release_date = request.POST['reldate']
        showupdater.desc = request.POST['description']
        showupdater.updated_at = datetime.datetime.now()
        networkupdater = request.POST['network']
        if Network.objects.filter(name=networkupdater).exists():
            showupdater.network = Network.objects.get(name=networkupdater)
        else:
            Network.objects.create(name=networkupdater)
            showupdater.network = Network.objects.get(name=networkupdater)
        showupdater.save()
        return redirect('/shows/' + str(show_id))

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == "POST":
        titl = request.POST['title']
        release = request.POST['reldate']
        description = request.POST['description']
        networkupdater = request.POST['network']
        if Network.objects.filter(name=networkupdater).exists():
            networkinput = Network.objects.get(name=networkupdater)
        else:
            Network.objects.create(name=networkupdater)
            networkinput = Network.objects.get(name=networkupdater)
        Show.objects.create(title=titl,release_date=release,desc=description,network=networkinput,updated_at=datetime.datetime.now())
        show_id = Show.objects.get(title=titl)
        return redirect('/shows/'+str(show_id.id))

def destroy(request, show_id):
    deleteme = Show.objects.get(id=show_id)
    deleteme.delete()
    return redirect('/shows')
