from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import User
from .forms import UserForm
from django.contrib.auth import authenticate

# Create your views here.


class login(View):
    def get(self, request):
        return render(request, 'login/login.html')

    def post(self, request):
        home = 'menus/home.html'
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = authenticate(username=username, password=password)
        if auth is None:
            return HttpResponse("401 Not Authorized")
        return HttpResponseRedirect('/home/')
