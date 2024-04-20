from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def home_view(request):
    return render(request, 'funding/home.html')

#def login_view(request):
#    form = AuthenticationForm(request, data=request.POST)
#    if form.is_valid():
#        user = form.get_user()
#        login(rquest, user)
#        return redirect('home')
#    else:
#        form = AuthenticationForm()
#    return render(request, 'founding/login.html', {'form': form})
def login_view(request):
    return render(request, 'funding/login.html')

def register_view(request):
    return render(request, 'funding/register.html')
