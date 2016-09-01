from django.conf.urls import url
from posts.views import PostListView, test_view


urlpatterns = [
    url(r'^$', PostListView.as_view(), name='posts'),
    url(r'^test/$', test_view, name='test'),
]
