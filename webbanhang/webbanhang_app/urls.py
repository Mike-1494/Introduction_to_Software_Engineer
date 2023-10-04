from django.urls import path
from . import views

urlpatterns = [
    path('mytemplate/', views.my_view, name='my_template'),
]