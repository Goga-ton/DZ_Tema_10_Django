from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Это ОсновнаЯ  страница моего домашнего задания в Django</h1>")

def page1(request):
    return HttpResponse("<h2>Это Моя Первая страница моего домашнего задания в Django</h2>")


def page2(request):
    return HttpResponse("<h2>Это Моя Вторая страница моего домашнего задания в Django</h2>")