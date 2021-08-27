from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('id/<str:cpv_id>', views.code, name='code'),
]

