from django.shortcuts import render

from .models import Post


def list_posts(request):
    post_list = Post.objects.order_by('-pub_date')
    context = {'post_list': post_list}
    return render(request, 'posts/index.html', context)
