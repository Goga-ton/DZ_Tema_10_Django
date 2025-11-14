from django.shortcuts import render, redirect
from .models import Films_stat
from .forms import Films_statForm
# Create your views here.
def films_stat(request):
    flst = Films_stat.objects.all()
    return render(request, 'films/films_stat.html', {'flsts': flst})

def film_create(request):
    error = ""
    if request.method == 'POST':
        form = Films_statForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fs')
        else:
            error = "Данные были заполнены не корректно"
    form = Films_statForm()
    return render(request, 'films/filmcreate.html',{'flcr': form, 'error': error})