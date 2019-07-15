from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomicideListView.as_view(), name='index'),
#    path('<int:homicide_id>', views.detail, name='detail'),
    path('<int:pk>/', views.HomicideDetailView.as_view(), name='detail'),
    path('<int:homicide_id>/article', views.article, name='article'),
]
