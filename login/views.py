from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import User
from .forms import UserForm
from django.contrib.auth import authenticate, login

# Create your views here.


class LoginView(View):
    def get(self, request):
        return render(request, 'login/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        my_user = authenticate(username=username, password=password)
        if my_user is not None:
            # login(request, my_user)
            return HttpResponseRedirect("/home/")

        return HttpResponse("401 Not Authorized")
