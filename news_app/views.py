from django.shortcuts import render, redirect
from .models import News
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def home(request):
    news_list = News.objects.all().order_by('-created_at')
    return render(request, 'news/index.html', {'news_list': news_list})
# Create your views here.
def index(request):
    return render(request, 'news_app/index.html')
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'news_app/register.html', {'form': form})