from django.urls import path
from . import views

app_name = 'pc_app'
urlpatterns = [
    path('', views.index, name='index'),
]
