from django.shortcuts import render
from django.http import Http404,HttpResponse
from .models import *


# Create your views here.
def starting_page(request):
    try:
        posts=Post.objects.all().order_by("-date")
        latest_post=posts[0:3]
        return render(request,"blog/starting_page.html",{'data':latest_post})
    except:
        return HttpResponse("error")



def post_page(request):
    sort_by_latest=Post.objects.all().order_by("-date")
    return render(request,"blog/allpost_page.html",{'data':sort_by_latest})

def parameter_post_page(request,slug):
    for x in Post.objects.all().order_by("-date"):
        print(x.author)
        if x.slug==slug:

            return render(request,"blog/postdetain_page.html",{'data':x,'tags':x.caption.all()})
    raise Http404()


    