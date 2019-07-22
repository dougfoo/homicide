from django.urls import path

from . import views

urlpatterns = [
    path('<int:homicide_id>/', views.detail, name='detail'),
    path('', views.HomicideListView.as_view(), name='index'),
    path('article/', views.ArticleListView.as_view(), name='article'),
    path('map/', views.MapView.as_view(), name='map'),
    path('chart_obj/', views.chart_obj, name='chart_obj'),
    path('chart_datetime/', views.chart_datetime, name='chart_datetime'),
    path('chart_stack/', views.chart_stack, name='chart_stack'),
    path('chart_mline/', views.chart_mline, name='chart_mline'),
    path('chart/', views.chart, name='chart'),
]
