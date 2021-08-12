from django.urls import path

from .views import index, detail, create, delete_task, delete_sub_task

app_name = 'polls'

urlpatterns = [
    path('', index, name='index'),
    path('<int:list_id>/', detail, name='list_details'),
    path('create/', create, name='list_create'),
    path("delete/<int:pk>/", delete_task, name="delete_task"),
    path("deleteItem/<pk>/", delete_sub_task, name="delete_sub_task"),
]