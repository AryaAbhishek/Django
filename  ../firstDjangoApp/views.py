from django.shortcuts import render
from django.http import HttpResponse
from firstDjangoApp.models import WebPage, AccessRecord, Topic
# Create your views here.

def initialize(request):
    WebPage_dict = AccessRecord.objects.order_by('date')
    date_dict = {'Access_Record':WebPage_dict}
    # my_dict = {'insert_me':"Hello i am inside views.py to test insert_me."}
    return render(request,'start.html',context = date_dict)
