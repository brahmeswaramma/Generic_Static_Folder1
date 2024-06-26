from django.shortcuts import render


# Create your views here.
def einstein(request):
    return render(request,'einstein.html')
