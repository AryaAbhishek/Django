from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'Hello USA!','number':200}
    return render(request, 'basic/index.html',context_dict)
def other(request):
    return render(request, 'basic/other.html')
def Relative(request):
    return render(request, 'basic/Relative_url_template.html')
