from django.shortcuts import redirect, render

from blog_app.forms import PostForm
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_at__isnull=False).order_by("-published_at")

    return render(
        request, 
        "post_list.html",
        {"posts":posts},
    )

def post_detail(request,pk):
    post = Post.objects.get(pk=pk, published_at__isnull=False)
    return render(
        request,
        "post_detail.html",
        {"post":post},
    )

from django.contrib.auth.decorators import login_required

@login_required
def draft_list(request):
    posts = Post.objects.filter(published_at__isnull=True)

    return render(
        request,
        "draft_list.html",
        {"posts":posts},
    )


from django.contrib.auth.decorators import login_required

@login_required
def draft_detail(request,pk):
    post = Post.objects.get(pk=pk,published_at__isnull=True)

    return render(
        request,
        "draft_detail.html",
        {"post":post},
    )

@login_required
def post_delete(request,pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect("post-list")

@login_required
def post_create(request):
    if request.method == "GET":
        form = PostForm()
        return render(
            request,
            "post_create.html",
            {"form":form},

        )
    
    else:
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect("draft-detail", pk=post.pk)
        
        else:
            return render(
                request,
                "post_create.html",
                {"form":form},
            )
    