from django.urls import path, re_path
from testapp import views

urlpatterns = [
    path('', views.index, name='index'),
]
