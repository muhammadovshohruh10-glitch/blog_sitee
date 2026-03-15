from django.urls import path
from .views import index_page
urlpatterns = [
    path('', index_page,name='my_app_list'),
]