from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createDirectory', views.createDirectory, name='createDirectory'),
    path('createDocument', views.createDocument, name='createDocument'),
]