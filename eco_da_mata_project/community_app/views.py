from django.shortcuts import render,redirect,get_object_or_404
from .models import Community, New
from .forms import CommunityForm
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import CommunitySerializer

class CommunityViewSet(viewsets.ReadOnlyModelViewSet)
    queryset = Community.objects.all()
    serializer_class = CommnuitySerializer

# Create your views here.
def create_community_view(request):     
    if request.method == "POST":
        form = CommunityForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
        return redirect ("RetrieveAllCommunityView")
    else:
        form = CommunityForm()
        context = {"form": form}
        return render(request,"form.html", context)

def retrieve_all_community_view(request):    
    community = Community.objects.all()
    context = {"comunidades": community}
    return render(request,"index.html",context)

def retrieve_community_view(request, community_id):     
    community = get_object_or_404(Community, pk = community_id)
    return HttpResponse(community.title + " " + str(community.id))

def update_community_view(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    if request.method == "POST":
        form = CommunityForm(request.POST, request.FILES, instance=community)
        if form.is_valid():
            form.save()
            return redirect("retrieve_all_community_view")
    else:
        form = CommunityForm(instance=community)
    context = {"form": form}
    return render(request, "form.html", context)    

def delete_community_view(request, community_id): 
    community = get_object_or_404(Community, pk=community_id)
    if request.method == "POST":
        form = forms.CommunityDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['Enviar']:
            form.delete()
            return redirect("index.html")  
    else:
        form = forms.CommunityDeleteForm()
    return render(request, 'communityform_delete.html', {'form': form, 'community': community})
    
