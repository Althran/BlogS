from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import TemplateView
from .forms import ContactForm
from .models import Post
from django.core.paginator import Paginator


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
    return render(request, 'index.html', {'posts': posts})


def post_detail(request, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post)
    return render(request, 'post_detail.html', {'post': post})


def about(request):
    return render(request, 'about.html')


# def contact(request):
#     return render(request, 'contact.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def contact_success_view(request):
    return render(request, 'contact_success.html')
