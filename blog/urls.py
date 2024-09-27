from django.urls import path
from . import views

urlpatterns = [
    path('<int>', views.blogDetail, name="blogDetailPage"),

]
