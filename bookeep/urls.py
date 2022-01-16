from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_name, name='home'),
    path('post/', views.post_data, name='post'),
    path('update/<id>', views.update, name='update'),
]