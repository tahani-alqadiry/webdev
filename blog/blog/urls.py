
from django.conf.urls import url
from django.contrib import admin
from post.views import Index,Detail,AllPosts, Blog,Create_post,Delete_post
from user_profile.views import Profile
# from post import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/(\w+)/$', Profile.as_view(), name="profile_detail"),
    url(r'^$',Index.as_view()),
    url(r'^posts/(?P<Category_id>[0-9]+)/$', Detail.as_view(),name="detail"),
    url(r'^posts/$', AllPosts.as_view()),
    url(r'^blog/(\w+)/$',Blog.as_view()),
    url(r'^posts/create/(\w+)/$',Create_post.as_view()),
    url(r'^posts/delete/(\w+)/$',Delete_post.as_view()),
    # url(r'^(\d{4}-\d{2}-\d{2})/$',AllPostsD.as_view()),



]
