from django.shortcuts import render,redirect,get_object_or_404
from .models import Community, New
from .forms import CommunityForm, CommunityDeleteForm
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import CommunitySerializer

class CommunityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

# Create your views here.
def create_community_view(request):     
    if request.method == "POST":
        form = CommunityForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
        return redirect ("retrieve_all_community_view")
    else:
        form = CommunityForm()
        return render(request,"community_form_create.html", context = {"form": form})

def retrieve_all_community_view(request):    
    community = Community.objects.all()
    return render(request,"community_index.html",context = {"comunidades": community})

def retrieve_community_view(request, community_id):     
    community = get_object_or_404(Community, pk = community_id)
    context = {"comunidade": community}
    print(community.title)
    return render(request,"community_index_retrieve.html",context=context)

def update_community_view(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    if request.method == "POST":
        form = CommunityForm(request.POST, request.FILES, instance=community)
        if form.is_valid():
            form.save()
            return redirect("retrieve_all_community_view")
    else:
        form = CommunityForm(instance=community)
    print(form)
    return render(request, "communityform_update.html", context = {"form": form})    

def delete_community_view(request, community_id): 
    community = get_object_or_404(Community, pk=community_id)
    if request.method == "POST":
        form = CommunityDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            community.delete()
            return redirect("retrieve_all_community_view")  
    else:
        form = CommunityDeleteForm()
    return render(request, 'communityform_delete.html', {'form': form, 'community': community})
    
