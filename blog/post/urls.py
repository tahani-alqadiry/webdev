
from django.conf.urls import url
from django.contrib import admin
from post.views import Detail,AllPosts, Blog, Create_post


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^posts/(?P<Category_id>[0-9]+)/$', Detail.as_view(),name="detail"),

    url(r'^posts/$', AllPosts.as_view(), name='all_posts'),

    url(r'^blog/(\w+)/$',Blog.as_view(), name='user_blog'),

    url(r'^user/posts/create/$',Create_post.as_view(), name='create_post'),




]
