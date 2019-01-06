from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Album
from django.template import loader

# Create your views here.

def index(request):
    all_albums = Album.objects.all()
    html = "<h1>List of Albums:</h1>"

    for i in all_albums:
        url = "/music/{}/".format(i.id)
        html += '<a href={}>{}</a><br>'.format(url, i.album_title)
    
    return HttpResponse(html)

def details(request,id):
    try:
        album = Album.objects.get(pk=id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist!")

    html = "<h2>Details of album id: {}<h2>".format(id)
    html += str(album).replace('\n','<br>')
    return HttpResponse(html)

