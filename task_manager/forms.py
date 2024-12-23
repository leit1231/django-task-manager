from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'priority', 'is_done', 'deadline']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название задачи'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Описание'}),
            'priority': forms.NumberInput(
                attrs={'class': 'form-control', 'min': 1, 'max': 10, 'placeholder': 'Приоритет (1-10)'}),
            'is_done': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'deadline': forms.DateTimeInput(
                attrs={
                    'class': 'form-control datetimepicker-input',
                    'data-target': '#datetimepicker-deadline',
                    'placeholder': 'Выберите дату и время',
                },
                format='%Y-%m-%d %H:%M:%S',
            ),

        }
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'priority': 'Приоритет',
            'is_done': 'Статус выполнения',
            'deadline': 'Дедлайн',
        }
