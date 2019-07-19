from django.urls import path

from . import views

urlpatterns = [
    path('<int:homicide_id>/', views.detail, name='detail'),
    path('', views.HomicideListView.as_view(), name='index'),
]
