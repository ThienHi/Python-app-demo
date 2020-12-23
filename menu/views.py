from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ListVideoForm
from .models import ListVideo
from django.contrib.auth import decorators

# Create your views here.


# @decorators.login_required()
def home(request):
    video = ListVideo.objects.all()
    return render(request, 'menus/home.html', {"video": video})


# @decorators.login_required()
def create(request):
    video = ListVideoForm()
    return render(request, 'menus/create.html', {"v": video})


# @decorators.login_required()
def save(request):
    if request.method == "POST":
        v = ListVideoForm(request.POST)
        if v.is_valid():
            v.save()
            # video = ListVideo.objects.all()
            return HttpResponseRedirect('/home/')
        else:
            return HttpResponse("Save False")
    else:
        return HttpResponse("Not Method POST")
