from django.views.generic import ListView, DetailView
from django.views.generic import CreateView
from.models import Post


class PostListView(ListView):
    template_name = "post_list.html"
    model = Post

class PostDetailedView(DetailView):
    template_name = "post_detail.html"
    model = Post 


class PostCreateView(CreateView):
    template_name = "post_new.html"
    model = Post
    fields = ["title", "body"]