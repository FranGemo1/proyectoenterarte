
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from .models import Event
from .forms import EventForm


def list_event(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'list_event.html', context)


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_events')
    else:
        form = EventForm()
    context = {'form': form}
    return render(request, 'create_event.html', context)

def update_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('list_events')
    else:
        form = EventForm(instance=event)
    context = {'form': form, 'event': event}
    return render(request, 'update_event.html', context)

def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('list_events')
    context = {'event': event}
    return render(request, 'delete_event.html', context)
