from django.shortcuts import render,get_object_or_404
from django.views import View
from user_profile.models import User
from .models import Post, Category


#show contents of index.html
class Index(View):
    def get(self, request):
        params = {}
        posts = Post.objects.all().order_by('-release_date')
        users = User.objects.all()
        categories = Category.objects.all()
        params['posts'] = posts
        params['users'] = users
        params['categories'] = categories
        return render(request, 'index.html', params)


# shows all posts in posts.html
class AllPosts(View):
    def get(self, request):
        params = {}
        posts = Post.objects.all().order_by('-release_date')
        params['posts'] = posts
        return render(request, 'posts.html', params)

#contents of blog/username
class Blog(View):
    def get(self, request, blogname):
        content = {}
        blog = User.objects.get(blog_name=blogname)
        posts = blog.post_set.all().order_by('-release_date')
        content['blog'] = blog
        content['posts'] = posts
        return render(request, 'user_blog.html',content)

# content of the blog post which is not applied yet
class Post_blog(View):
    def get(self, request, postname):
        content = {}
        post = Post.objects.get(title=postname)
        content['post'] = post
        return render(request, 'user_post.html',content)


# the category details of post
class Detail(View):
    def get(self,request, Category_id):
        category = get_object_or_404(Category, id=Category_id)
        return render(request, 'categ_detail.html', {'category': category})


class Create_post(View):
    def get(self,request,post_name):
        try:
            obj = Post.objects.get(title=post_name)
            content = {'post': obj}
            content['msg'] = "The post title exists try another one"
            return render(request, 'create.html', content)
        except Post.DoesNotExist:
            c = Category.objects.get(title='news')
            user = User.objects.get(username='tahani')
            obj = Post(content="this is created by user tahani", category=c, title=post_name, author=user, is_active=True)
            obj.save()
            content = {'post': obj}
            return render(request, 'create.html', content)



class Delete_post(View):
    def get(self,request,post_name):
        try:
            obj = Post.objects.get(title=post_name).delete()
            content = {}
            content['msg'] = "The post is deleted!"
            return render(request, 'delete.html', content)
        except Post.DoesNotExist:
            content = {}
            content['msg'] = "The post doesn't exist!"
            return render(request, 'delete.html', content)



# content = {}
# post = Post.objects.get(title=post_name)
# if post:
#     user = User.objects.get(username=post.author)
#     content['post'] = post
#     content['user'] = user
#     return render(request, 'user_blog.html', content)
# else:
#     user = User.objects.get(username='tahani')
#     content['user'] = user
#     return render(request, 'create.html', content)



# class Blog_content(View):
#     def get(self, request, username):
#         params = {}
#         user = User.objects.get(username=username)
#         posts = Post.objects.filter(author=user).order_by('-release_date')
#         params['posts'] = posts
#         params['author'] = user
#         return render(request,'user_blog.html', params)



# class Blog_content(View):
#     def get(self, request,username):
#         author = get_list_or_404(User, username=username)
#         return render(request, 'user_blog.html', {'author': author})
