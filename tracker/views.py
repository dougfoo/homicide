from django.http import HttpResponse
from .models import Article, Homicide
from django.template import loader
from django.shortcuts import get_object_or_404, render

def index(request):
    h_list = Homicide.objects.order_by('-date')[:5]
    template = loader.get_template('tracker/index.html')
    context = { 'h_list': h_list, }
    return HttpResponse(template.render(context, request))
    # return render(request, 'tracker/index.html', context)

def detail(request, homicide_id):
    homicide = get_object_or_404(Homicide, pk=homicide_id)
    return render(request, 'tracker/detail.html', {'homicide': homicide})

def article(request, homicide_id):
    return HttpResponse("You're looking at articles for homicide %s." % homicide_id)

