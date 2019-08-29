from django.shortcuts import render

# Create your views here.

def index(request):
    context={
        'hello': 'hello World',
    }
    return render(request,'core/index.html',context)