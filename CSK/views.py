from django.shortcuts import render

# Create your views here.
def yellow(request):
    return render(request,'yellow.html')
