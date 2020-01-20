from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm
from posts.models import Posts
# Create your views here.
@login_required
def list_posts(request):
    post = Posts.objects.all().order_by('-created')
    return render(request = request,
                  template_name ='posts/feed.html',
                  context = {'posts' : post
                            }
                 )

@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()

    return render(request = request,
                  template_name = 'posts/new_post.html',
                  context = {
                      'form' : form,
                      'user' : request.user,
                      'profile' : request.user.profile
                    }
                )
