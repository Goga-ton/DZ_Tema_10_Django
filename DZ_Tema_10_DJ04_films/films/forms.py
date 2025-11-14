from .models import Films_stat
from django.forms import ModelForm, Textarea, TextInput, DateTimeInput

class Films_statForm(ModelForm):
    class Meta:
        model = Films_stat
        fields = ['title', 'description', 'feedback']
        widgets = {
            'title': TextInput(attrs={'class':'form-control', 'placeholder':'Введите название фильма'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder':'Введите описание фильма'}),
            'feedback': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите отзыв'}),

        }