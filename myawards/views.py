from django.shortcuts import render
from .forms import  SignupForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def signup(request):
    form = SignupForm
    return render(request, 'registration/signup.html', {'form': form})