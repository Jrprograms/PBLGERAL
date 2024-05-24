from django.shortcuts import render,redirect,get_object_or_404
from .models import Community, New
from .forms import CommunityForm
from django.http import HttpResponse

# Create your views here.
def create_community_view(request):     #create
    if request.method == "POST":
        form = CommunityForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
        return redirect ("RetrieveAllCommunityView")
    else:
        form = CommunityForm()
        context = {"form": form}
        return render(request,"form.html",context)

def retrieve_all_community_view(request):     #getall
    community = Community.objects.all()
    context = {"comunidades": community}
    return render(request,"index.html",context)

def retrieve_community_view(request, community_id):     #get
    community = get_object_or_404(Community, pk = community_id)
    return HttpResponse(community.title + " " + str(community.id))

def delete_community_view(request, community_id):
    if request.method == "POST":
    community = get_object_or_404(Community, pk=community_id) #se der o erro ele para aqui ou exclui o nada?
    if request.method == "POST":
        form = forms.CommunityDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['Enviar']:
            form.delete()
        return redirect("RetrieveAllCommunityView")  
    else:
        return HttpResponseForbidden("Não é possível deletar esta comunidade")
    
