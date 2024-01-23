from django.urls import path
from . import views

urlpatterns =[
path('Search/',views.search_coin),
path('Mills/',views.playMills)

]
