from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index( request):
    # return HttpResponse("<h1>Это ОсновнаЯ  страница моего домашнего задания в Django</h1>")
    return render(request, 'page/page1.html')

def fpage1(request):
    # return HttpResponse("<h2>Это Моя Первая страница моего домашнего задания в Django</h2>")
    return render(request, 'page/page2.html')

def fpage2(request):
    # return HttpResponse("<h2>Это Моя Вторая страница моего домашнего задания в Django</h2>")
    return render(request, 'page/page3.html')

def fpage3(request):
    return render(request, 'page/page4.html')