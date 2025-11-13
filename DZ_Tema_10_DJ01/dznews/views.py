from django.shortcuts import render
from .models import DZ_News_post

# Create your views here.
def dz_news_1(request):
    news = DZ_News_post.objects.all()
    return render(request, 'dznews/dznews_1.html' , {'news' : news})