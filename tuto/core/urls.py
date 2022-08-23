from django.urls import path
from .views import *

app_name = 'core'
urlpatterns = [
    path('', BasePageView.as_view(), name='base'),
    path('dashboard/', DashboardPageView.as_view(), name='dashboard'),
]
