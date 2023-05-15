from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Event:
        model = Event
        fields = ['tittle', 'price', 'description', 'location']
