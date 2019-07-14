from django.http import HttpResponse
from .models import Article, Homicide
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views import generic

def index(request):
    h_list = Homicide.objects.order_by('-date')[:5]
    template = loader.get_template('tracker/index.html')
    context = { 'h_list': h_list, }
    return HttpResponse(template.render(context, request))
    # return render(request, 'tracker/index.html', context)

class DetailView(generic.DetailView):
    model = Homicide
    template_name = 'tracker/detail.html'

def article(request, homicide_id):
    article = get_object_or_404(Article, pk=homicide_id)
    return render(request, 'tracker/article.html', {'article': article})
