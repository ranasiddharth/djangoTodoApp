from django.urls import path

from .views import index, detail, create

app_name = 'polls'

urlpatterns = [
    path('', index, name='index'),
    path('<int:list_id>/', detail, name='list_details'),
    path('create/', create, name='list_create'),
]