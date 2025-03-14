from django.shortcuts import render
from django.views import generic
from .models import Post


def blog_home(request):
    return render(request, 'blog/home.html')

# Create your views here.
class Postlist(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6