from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('document', views.createDocument, name='createDocument'),
    path('document/directory', views.createDirectory, name='createDirectory'),
    path('document/directory/all', views.findAllDirectory, name='findAllDirectory'),
]
