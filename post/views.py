from django.shortcuts import render,HttpResponse, get_object_or_404, HttpResponseRedirect,redirect
from .models import Post
from .forms import Postform
from django.contrib import messages

# Create your views here.

def post_index(request):
    posts=Post.objects.all()
    return render(request, "post/post_index.html",{'posts':posts}) 

def post_detail(request,id):
    post=get_object_or_404(Post, id=id)

    context={
        'post':post
    }
    return render(request, "post/post_detail.html",context)

def post_create(request):
   

    #if request.method=="POST":
    #    print(request.POST)
    
    #title=request.POST.get('title')
    #content=request.POST.get('context')
    #Post.objects.create(title=title, context=content )


    if request.method=="POST":
        form = Postform(request.POST)
        if form.is_valid():
            post=form.save()
            messages.success(request,'Başarılı bir şekilde oluşturdunuz')
            messages.success(request,'Başarılı bir şekilde oluşturdunuz')
            messages.success(request,'Başarılı bir şekilde oluşturdunuz')
            return HttpResponseRedirect(post.get_absolute_url())
    else:
          form = Postform

    #form=Postform(request.POST or None)
    #if form.is_valid():
    #    form.save()

    context={
        'form':form,
    }

    return render(request, "post/post_create.html",context)

def post_update(request,id):
    post=get_object_or_404(Post, id=id)
    form=Postform(request.POST or None, instance=post)
    if form.is_valid():
            form.save()
            messages.success(request,'Başarılı bir şekilde oluşturdunuz')
            messages.success(request,'Başarılı bir şekilde oluşturdunuz')
            messages.success(request,'Başarılı bir şekilde oluşturdunuz')
            return HttpResponseRedirect(post.get_absolute_url())
    context={
        'form':form,
    }     
    return render(request, "post/post_create.html",context)

def post_delete(request,id):
    post=get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post:index')


