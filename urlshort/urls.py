from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<code>/', views.shorting_view, name='shorting_view'),

]
