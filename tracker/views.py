from django.http import HttpResponse, JsonResponse
from .models import Article, Homicide
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.db.models.functions import TruncMonth
from django.db.models import Count, Sum, Avg
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
    queryset = Homicide.objects.all().order_by('count')
    context_object_name = 'h_list'

def chart_obj(request):
    h_list = Homicide.objects.annotate(c=Count('count')).values('age','c','gender')
    data = alt.Data(values=list(h_list))
    chart = alt.Chart(data, height=300, width=300, title='Age / Gender').mark_circle().encode(
        x='age:Q',
        y='gender:N',
        size='sum(c):Q'
    )
    return JsonResponse(chart.to_dict(), safe=False)

def chart_datetime(request):
    h_list = Homicide.objects.only('date','time','gender','age','means','location').values()
    data = alt.Data(values=list(h_list))

    chart = alt.Chart(data, title='Date vs Time').mark_circle(size=60).encode(
        x='date:T',
        y='time:O',
        color='gender:N',
        tooltip=['age:Q', 'means:N', 'ethnicity:N', 'location:N', 'time:O']
    ).interactive()
    return JsonResponse(chart.to_dict(), safe=False)

def chart_stack(request):
    h_list = Homicide.objects.annotate(month=TruncMonth('date')).values('month').annotate(count=Count('count')).values('month','count','gender')
    data = alt.Data(values=list(h_list))

    chart = alt.Chart(data, height=300, width=300, title='Month Count by Gender').mark_bar().encode(
        x='month:N',
        y='count:Q',
        color='gender:N'
    ).interactive()
    return JsonResponse(chart.to_dict(), safe=False)

def chart_mline(request):
    h_list = Homicide.objects.annotate(month=TruncMonth('date')).values('month').annotate(count=Count('count')).values('month','count','ethnicity')
    data = alt.Data(values=list(h_list))

    chart = alt.Chart(data, height=300, width=300, title='Month Count by Ethnicity').mark_line(size=1).encode(
        x='month:N',
        y='count:Q',
        color='ethnicity:N'
    ).interactive()
    return JsonResponse(chart.to_dict(), safe=False)

def chart(request):
    return render(request, "tracker/chart.html", {})

