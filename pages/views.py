from django.shortcuts import render
from django.http import HttpResponse
from users.models import User

# Create your views here.
def index(request):
    users = User.objects.all()[:4]
    context={
        'users': users,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')