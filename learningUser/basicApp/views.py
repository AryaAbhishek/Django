from django.shortcuts import render
from basicApp.forms import UserInfo, UserInfoModelForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'basicApp/index.html')

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserInfo(data=request.POST)
        portfolio_form = UserInfoModelForm(data=request.POST)

        if user_form.is_valid() and portfolio_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            portfolio = portfolio_form.save(commit=False)
            portfolio.user = user

            if 'portfolio_image' in request.FILES:
                portfolio.portfolio_image = request.FILES['portfolio_image']

            portfolio.save()
            registered = True
        else:
            print(user_form.errors,portfolio_form.errors)
    else:
        user_form = UserInfo()
        portfolio_form = UserInfoModelForm()
    return render(request, 'basicApp/registration.html',
                {'user_form':user_form,'portfolio_form':portfolio_form,
                'registered':registered})
