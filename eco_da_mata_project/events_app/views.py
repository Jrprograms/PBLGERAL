from django.shortcuts import render,redirect,get_object_or_404
from .models import event
from .forms import event_form


# Create your views here.

def create_event(request):
    if request.method == "POST":
        form = event_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect ('getEvents')
    else:
        form = event_form()
        context = {"form": form}
        return render(request,"eventform.html",context)
    
def getEvents(request):
    events = event.objects.all()
    context = {"Eventos": events}
    return render(request,"eventindex.html",context)