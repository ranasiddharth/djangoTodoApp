from django.urls import path

from .views import index, detail, create, delete_task, delete_sub_task, createsub, update_task, update_sub_task

app_name = 'polls'

urlpatterns = [
    path('', index, name='index'),
    path('<int:list_id>/', detail, name='list_details'),
    path('create/', create, name='list_create'),
    path("delete/<int:pk>/", delete_task, name="delete_task"),
    path("deleteItem/<int:pk>/", delete_sub_task, name="delete_sub_task"),
    path("createItem/<int:pk>", createsub, name="createsub"),
    path("update/<int:pk>/", update_task, name="update_task"),
    path("update_sub/<int:pk>/", update_sub_task, name="update_sub_task"),
]