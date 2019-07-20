from django.urls import path

from . import views

urlpatterns = [
    path('<int:homicide_id>/', views.detail, name='detail'),
    path('', views.HomicideListView.as_view(), name='index'),
    path('article/', views.ArticleListView.as_view(), name='article'),
    path('map/', views.MapView.as_view(), name='map'),
]
