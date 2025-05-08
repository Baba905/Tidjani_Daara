from django.urls import path
from Daara import views

urlpatterns =[
    path("", views.home, name="home"),
    path("upload/",views.upload_file,name='upload_file'),
    path("library/", views.list_of_documents, name='library'),
    path("delete/<int:pk>", views.delete_document, name='delete_document'),
    path("summary/<int:pk>", views.summarize, name='summary'),
]