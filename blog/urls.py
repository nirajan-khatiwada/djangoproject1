from django.urls import path
from . import views
urlpatterns = [path("post/",views.post_page,name='allpost'),
               path("post/<slug:slug>/",views.parameter_post_page,name="postpage"),
               path("",views.starting_page,name="home")]
