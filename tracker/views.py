from django.http import HttpResponse, JsonResponse
from .models import Article, Homicide
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views import generic
import altair as alt

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

def chart_obj(request):
    h_list = Homicide.objects.only('date','age','gender').values()
#    print('hlist',type(h_list), str(h_list))
    data = alt.Data(values=list(h_list))
#    print('\n\n**data',type(data), str(data))
    chart = alt.Chart(data).mark_point().encode(
        x='age:Q',
        y='date:T',
        color='gender:N',
    )
    print('\n\n**chart',type(chart), str(chart))
    return JsonResponse(chart.to_dict(), safe=False)

def chart(request):
    return render(request, "tracker/chart.html", {})

