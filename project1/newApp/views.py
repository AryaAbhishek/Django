from django.shortcuts import render
# from django.http import HttpResponse
# from newApp.models import User
from newApp.forms import NewUser
# Create your views here.

def start(request):
    # new_dict = {'include_me':'GOTO user/ to check users details.'}
    # return render(request,'start.html',context = new_dict)
    return render(request,'start.html')

def user(request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return start(request)
        else:
            print("form invalid.")
    return render(request, "users.html", {'form':form})
    # user_dic = User.objects.order_by('FirstName')
    # details_dict = {'details':user_dic}
    # return render(request,'users.html',context = details_dict)
