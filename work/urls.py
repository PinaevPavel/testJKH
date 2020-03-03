from django.urls import path
from .import views

app_name = 'work'

urlpatterns = [
	path('', views.view, name='view'),
	path('reset/', views.reset, name='reset' )
]