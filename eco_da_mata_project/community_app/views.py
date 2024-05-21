from django.shortcuts import render,redirect
from .models import Community, New
from .forms import CommunityForm

# Create your views here.
def CreateCommunityView(request):
    if request.method == "POST":
        form = CommunityForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect ("RetrieveCommunityView")
    else:
        form = CommunityForm()
        context = {"form": form}
        return render(request,"form.html",context)

def RetrieveCommunityView(request):
    comunidades = Community.objects.all()
    context = {"comunidades": comunidades}
    return render(request,"index.html",context)
  

  


