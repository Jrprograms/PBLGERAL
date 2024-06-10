from django.shortcuts import render,redirect,get_object_or_404
from .models import Community, New
from .forms import CommunityForm, CommunityDeleteForm,NewsDeleteForm,NewsForm
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import CommunitySerializer, NewSerializer

class CommunityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

# Community views
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
    return render(request, "community_form_update.html", context = {"form": form})    

def delete_community_view(request, community_id): 
    community = get_object_or_404(Community, pk=community_id)
    if request.method == "POST":
        form = CommunityDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            community.delete()
            return redirect("retrieve_all_community_view")  
    else:
        form = CommunityDeleteForm()
    return render(request, 'community_form_delete.html', {'form': form, 'community': community})


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer
# News views
def retrieve_all_news_view(request):
    News = New.objects.all()
    return render(request,"news_index.html",context = {"noticias": News})

def retrieve_news_view(request, news_id):     
    news = get_object_or_404(New, pk = news_id)
    context = {"noticia": news}
    return render(request,"news_index_retrieve.html",context=context)

def create_news_view(request):     
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
        return redirect ("retrieve_all_news_view")
    else:
        form = NewsForm()
        return render(request,"news_form_create.html", context = {"form": form})
    
def update_news_view(request, news_id):
    news = get_object_or_404(New, pk=news_id)
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect("retrieve_all_news_view")
    else:
        form = NewsForm(instance=news)
    print(form)
    return render(request, "news_form_update.html", context = {"form": form})

def delete_news_view(request, news_id): 
    news = get_object_or_404(New, pk=news_id)
    if request.method == "POST":
        form = NewsDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            news.delete()
            return redirect("retrieve_all_news_view")  
    else:
        form = NewsDeleteForm()
    return render(request, 'news_form_delete.html', {'form': form, 'news': news})
