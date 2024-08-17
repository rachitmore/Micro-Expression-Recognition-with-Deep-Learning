from django.urls import path
from . import views

app_name = 'micro_expression'

urlpatterns = [
    path('', views.home, name='home'),

]
