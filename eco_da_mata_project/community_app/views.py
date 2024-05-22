from django.shortcuts import render,redirect,get_object_or_404
from .models import Community, New
from .forms import CommunityForm
from django.http import HttpResponse

# Create your views here.
def create_community_view(request):
    if request.method == "POST":
        form = CommunityForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect ("RetrieveAllCommunityView")
    else:
        form = CommunityForm()
        context = {"form": form}
        return render(request,"form.html",context)

def retrieve_all_community_view(request):
    community = Community.objects.all()
    context = {"comunidades": community}
    return render(request,"index.html",context)

def retrieve_community_view(request, community_id):
    community = get_object_or_404(Community, pk = community_id)
    return HttpResponse(community.title + " " + str(community.id))
