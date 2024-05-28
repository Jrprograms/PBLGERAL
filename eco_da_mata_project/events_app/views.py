from django.shortcuts import render,redirect,get_object_or_404, HttpResponse
from .models import Event
from .forms import event_form, deleteeventform


# Create your views here.

def create_event(request):
    if request.method == "POST":
        form = event_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print('FORMULÁRIO SALVO')
        else:
            print('FORMULÁRIO NAO SALVO')
        return redirect ('get_events')
    else:
        form = event_form()
        context = {"form": form}
        return render(request,"event_form.html",context)


def get_events(request):
    events = Event.objects.all()
    context = {"events": events}
    return render(request,"event_list.html",context)


def get_single_event(request, event_id): 
    event = get_object_or_404(Event, pk = event_id)
    return render(request, "single_event.html", {"event":event})


def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = event_form(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('../../list/', event_id=event.id)
    else:
        form = event_form(instance=event)
    return render(request, 'edit_event.html', {'form': form, 'event': event})


def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('get_events')
    return render(request, 'delete_event_form.html', {'event': event})

