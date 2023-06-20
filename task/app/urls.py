from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tasks/", views.TaskViewSet.as_view({'get': 'list'})),
    path("tasks/remaining", views.TaskViewSet.as_view({'get': 'list_remaining'})),
    path("tasks/<int:pk>", views.TaskViewSet.as_view({'get': 'retrieve'})),
    path("tasks/create", views.TaskViewSet.as_view({'post' : 'create'})),
    path("tasks/update/<int:pk>", views.TaskViewSet.as_view({'patch': 'partial_update'})),
    path("tasks/delete/<int:pk>", views.TaskViewSet.as_view({'delete': 'destroy'})),
    path("tasks/complete/<int:pk>", views.TaskViewSet.as_view({'post': 'complete'}))
]