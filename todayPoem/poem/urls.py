from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:poem_id>/',views.view,name='view'),
]