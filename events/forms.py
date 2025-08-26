from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'location', 'start_time', 'end_time', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'イベント名を入力してください'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '場所を入力してください'
            }),
            'start_time': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'end_time': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'イベントの詳細を入力してください'
            })
        }
        labels = {
            'title': 'イベント名',
            'location': '場所',
            'start_time': '開始日時',
            'end_time': '終了日時',
            'description': '詳細'
        }
