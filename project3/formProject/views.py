from django.shortcuts import render

# Create your views here.
# from . import forms
from formProject import forms

def index(request):
    return render(request, 'form.html')

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("form validation is successful.")
            print("NAME "+ form.cleaned_data['name'])
            print("EMAIL "+ form.cleaned_data['email'])
            print("TEXT " + form.cleaned_data['text'])

    return render(request, "form_page.html", {'form':form})
