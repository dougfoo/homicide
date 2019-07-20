from django.http import HttpResponse
from .models import Article, Homicide
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views import generic

class HomicideListView(generic.ListView):
    model = Homicide
    template_name = 'tracker/detail.html'
    queryset = Homicide.objects.all().order_by('-count')
    context_object_name = 'h_list'

def detail(request, homicide_id):
    homicide = get_object_or_404(Homicide, pk=homicide_id)
    h_list = Homicide.objects.all().order_by('-date')
    return render(request, 'tracker/detail.html', {'h_list': h_list, 'homicide': homicide })

class ArticleListView(generic.ListView):
    model = Article
    template_name = 'tracker/article.html'
    queryset = Article.objects.all()
    context_object_name = 'h_list'

class MapView(generic.ListView):
    model = Homicide
    template_name = 'tracker/map.html'
    queryset = Homicide.objects.all().order_by('-count')
    context_object_name = 'h_list'
