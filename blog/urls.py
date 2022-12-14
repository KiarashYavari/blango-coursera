from django.urls import path
import blog.views

app_name= "blog"

urlpatterns = [
    path("", blog.views.index),
    path("post/<slug>/", blog.views.post_detail, name="blog-post-detail"),
     
]
