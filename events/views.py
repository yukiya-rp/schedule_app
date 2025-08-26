from django.shortcuts import render
from .models import Event

def event_list(request):
    events = Event.objects.all().order_by('start_time')
    return render(request, 'events/event_list.html', {'events': events})