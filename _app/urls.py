from django.urls import path
from . import views

urlpatterns = [
	path('', views.main, name='main'),
	path('func/<str:func_name>', views.func_view, name='func'),
]