from django.http import HttpResponse, JsonResponse
from .models import Article, Homicide
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.db.models.functions import TruncMonth
from django.db.models import Count, Sum, Avg
import altair as alt
import pandas as pd
import numpy as np

# still used but should migrate to single detail view ??
class HomicideListView(generic.ListView):
    model = Homicide
    template_name = 'tracker/detail.html'
    queryset = Homicide.objects.all().order_by('-date')
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
        alt.X('age:Q',bin=True),
        alt.Y('gender:N'),
        alt.Size('sum(c):Q',title='Counts'),
        color='sum(c):Q'
    )
    return JsonResponse(chart.to_dict(), safe=False)

def chart_datetime(request):
    h_list = Homicide.objects.only('date','time','gender','age','means','location').values()
    data = alt.Data(values=list(h_list))

    chart = alt.Chart(data, title='Date vs Time').mark_circle(size=60).encode(
        alt.X('date:T'),
        alt.Y('time:O'),
        color='gender:N',
        tooltip=['age:Q', 'means:N', 'ethnicity:N', 'location:N', 'time:O']
    ).interactive()
    return JsonResponse(chart.to_dict(), safe=False)

def chart_stack(request):
    h_list = Homicide.objects.annotate(month=TruncMonth('date')).values('month').annotate(ct=Count('count')).values('month','ct','gender')
    data = alt.Data(values=list(h_list))

    chart = alt.Chart(data, height=300, width=300, title='Month Count by Gender').mark_bar(size=30).encode(
        x='month:T',
        y='ct:Q',
        color='gender:N'
    ).interactive()
    return JsonResponse(chart.to_dict(), safe=False)

def chart_mline(request):
    h_list = Homicide.objects.annotate(month=TruncMonth('date')).values('month').annotate(ct=Count('count')).values('month','ct','ethnicity')
    data = alt.Data(values=list(h_list))

    chart = alt.Chart(data, height=300, width=300, title='Month Count by Ethnicity').mark_bar(size=30,opacity=0.7).encode(
        x='month:T',
        y='ct:Q',
        color='ethnicity:N'
    ).interactive()
    return JsonResponse(chart.to_dict(), safe=False)

def chart_suspect(request):
    h_list = Homicide.objects.annotate(ct=Count('count')).values('ethnicity','killerethnicity','ct').annotate(s=Sum('ethnicity'))
    data = alt.Data(values=list(h_list))

    chart = alt.Chart(data, height=300, width=300, title='Culprit vs Victim').mark_rect().encode(
        alt.X('ethnicity:N',title='victim ethnicity'),
        alt.Y('killerethnicity:N',title='culprit ethnicity'),
        color='ct:Q',
        tooltip=['ct:Q']
    ).interactive()
    return JsonResponse(chart.to_dict(), safe=False)

def chart_trend(request):
    h_list = Homicide.objects.annotate(month=TruncMonth('date')).values('month','id')
    data = alt.Data(values=list(h_list))

    chart = alt.Chart(data,height=300, width=300, title='Cumulative Count').transform_window(
        sort=[{'field': 'month'}],
        frame=[None, 0],
        cumulative_count='count(id)',
    ).mark_area().encode(
        x='month:T',
        y='cumulative_count:Q',
    )
    return JsonResponse(chart.to_dict(), safe=False)

def chart_regression(request):
    h_list = Homicide.objects.annotate(month=TruncMonth('date')).values('month').annotate(ct=Count('count')).values('month','ct')
    df = pd.DataFrame(list(h_list))
    df['cum'] = df['ct'].cumsum()
    df['i'] = df.index+1   # 1 is start of year
    df = df.drop(columns=['month','ct'])

    # Define the degree of the polynomial fit
    degree_list = [1, 2, 3]

    # break into baby steps for graph
    poly_data = pd.DataFrame({'xfit': np.linspace(df['i'].min(), 12, 500)})  # 12 is end of year

    for degree in degree_list:
        poly_data[str(degree)] = np.poly1d(np.polyfit(df['i'], df['cum'], degree))(poly_data['xfit'])

    # Tidy the dataframe so 'degree' is a variable
    poly_data = pd.melt(poly_data,
                        id_vars=['xfit'],
                        value_vars=[str(deg) for deg in degree_list],
                        var_name='degree', value_name='yfit')

    # Plot the data points on an interactive axis
    points = alt.Chart(df,title='Polynomial Regression Predictions').mark_circle(color='black').encode(
        x=alt.X('i', title='months'),
        y=alt.Y('cum', title='cumulative murder count')
    ).interactive()

    # Plot the best fit polynomials
    polynomial_fit = alt.Chart(poly_data).mark_line().encode(
        x='xfit',
        y='yfit',
        color=alt.Color('degree',title='Model'),
        tooltip=[alt.Tooltip('yfit',title='predicted homicides'),alt.Tooltip('xfit',title='Month')]
    )

    chart = points + polynomial_fit
    return JsonResponse(chart.to_dict(), safe=False)

def chart(request):
    return render(request, "tracker/chart.html", {})

def fetch_article(request, eurl):
    from goose3 import Goose
    import base64 as b64
    print('eurl',eurl)
    url = b64.b64decode(eurl).decode('ascii')
    print('decoded', url)

    g=Goose()
    article = g.extract(url=url)
    my_dict = [{'heading': article.title, 'meta': article.meta_description, 'body': article.cleaned_text}]
    return JsonResponse(my_dict, safe=False)

