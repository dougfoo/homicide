from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers, serializers, viewsets
from . import views
from .models import Homicide

class HomicideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homicide
        fields = ['age', 'articles',
                  'count',
                  'date',
                  'ethnicity',
                  'gender',
                  'id',
                  'intersection',
                  'killerage',
                  'killerethnicity',
                  'killergender',
                  'killername',
                  'location',
                  'mapiframe',
                  'means',
                  'motive',
                  'name',
                  'street',
                  'time']

# ViewSets define the view behavior.
class HomicideViewSet(viewsets.ModelViewSet):
    queryset = Homicide.objects.all()
    serializer_class = HomicideSerializer

hrouter = routers.DefaultRouter()
hrouter.register(r'homicides', HomicideViewSet)

urlpatterns = [
    path('<int:homicide_id>/', views.detail, name='detail'),
    path('', views.HomicideListView.as_view(), name='index'),
    path('map/', views.MapView.as_view(), name='map'),
    path('chart_obj/', views.chart_obj, name='chart_obj'),
    path('chart_heat/', views.chart_heat, name='chart_heat'),
    path('chart_stack/', views.chart_stack, name='chart_stack'),
    path('chart_mline/', views.chart_mline, name='chart_mline'),
    path('chart_suspect/', views.chart_suspect, name='chart_suspect'),
    path('chart_cum/', views.chart_cum, name='chart_cum'),
    path('chart_regression/', views.chart_regression, name='chart_regression'),
    path('chart_tod/', views.chart_tod, name='chart_tod'),
    path('chart_cod/', views.chart_cod, name='chart_cod'),
    path('chart/', views.chart, name='chart'),
    path('fetch_article/<str:eurl>/', views.fetch_article, name='fetch_article'),
    url(r'^', include(hrouter.urls)),
    path('jsondata/', views.jsondata, name='jsondata'),
    path('csvdata/', views.csvdata, name='csvdata'),
]
