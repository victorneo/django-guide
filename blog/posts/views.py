from django.shortcuts import render
from django.views.generic import ListView
from posts.models import Post


class PostListView(ListView):
    model = Post


def test_view(request):
    return render(request, 'posts/post_list.html')
