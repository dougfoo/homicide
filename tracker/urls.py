from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
#    path('<int:homicide_id>', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:homicide_id>/article', views.article, name='article'),
]
