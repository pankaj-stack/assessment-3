from django.urls import path
from .views import post_list,post_detail
urlpatterns = [
    path('',post_list, name='list'),
    path('delete/<int:pk>/',post_detail,name='detail'),
]
