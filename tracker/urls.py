from django.urls import path

from . import views

urlpatterns = [
    path('<int:homicide_id>/', views.detail, name='detail'),
    path('', views.HomicideListView.as_view(), name='index'),
    path('article/', views.ArticleListView.as_view(), name='article'),
    path('map/', views.MapView.as_view(), name='map'),
    path('chart_obj/', views.chart_obj, name='chart_obj'),
    path('chart_heat/', views.chart_heat, name='chart_heat'),
    path('chart_stack/', views.chart_stack, name='chart_stack'),
    path('chart_mline/', views.chart_mline, name='chart_mline'),
    path('chart_suspect/', views.chart_suspect, name='chart_suspect'),
    path('chart_trend/', views.chart_trend, name='chart_trend'),
    path('chart_regression/', views.chart_regression, name='chart_regression'),
    path('chart_tod/', views.chart_tod, name='chart_tod'),
    path('chart/', views.chart, name='chart'),
    path('fetch_article/<str:eurl>/', views.fetch_article, name='fetch_article'),
]
