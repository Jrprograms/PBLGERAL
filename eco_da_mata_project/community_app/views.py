from django.shortcuts import render
from .models import Community, New
from .forms import CommunityForm

# Create your views here.
def CreateCommunityView(request):
    if request.method == "POST ":
        form = CommunityForm(request.POST)
        if form.is_valid():
            form.save()
        return render (request,"index.html") # Ideal é que seja usado o redirect ao invés do render neste caso.
    else:
        form = CommunityForm()
        context = {"form": form}
        return render(request,"form.html",context)

def RetrieveCommunityView(request):
    comunidades = Community.objects.all()
    context = {"comunidades": comunidades}
    return render(request,"index.html",context) # Cuidado com nomes genéricos para templates. Pode dar conflito se outro aplicativo acessar o mesmo nome.
  


