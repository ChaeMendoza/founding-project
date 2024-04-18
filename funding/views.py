from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'funding/home.html')

def login_view(request):
    return render(request, 'funding/login.html')

def register_view(request):
    return render(request, 'funding/register.html')