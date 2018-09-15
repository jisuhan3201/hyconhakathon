from django.urls import path
from . import views

app_name = "papers"
urlpatterns = [
    path("", view=views.all_papers, name="all_pages"),
]
