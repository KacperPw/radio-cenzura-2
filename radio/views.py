from django.shortcuts import render, get_object_or_404
from .models import Category, Subcategory, Post, PostIndex
from .models import Event
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



from django.utils.safestring import mark_safe


def index(request):
    posts = Post.objects.all().order_by('-pub_date')[:5]
    post_index = PostIndex.objects.all().order_by('-id')
    
    paginator = Paginator(post_index, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'posts': posts, 'post_index': post_index, 'page_obj': page_obj}
    return render(request, 'index.html', context)


def events_list(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})


def post_index_details(request, id):
    post_index = PostIndex.objects.get(id=id)
    
    context = {'post_index': post_index}
    return render(request, 'post_index_details.html', context)



def post_details(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    context = {'post': post}
    return render(request, 'post_details.html', context)


def archive(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'archive.html', context)


def subcategories(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    subcategories = category.subcategory_set.all()  # zmiana z category.subcategories na category.subcategory_set
    context = {'category': category, 'subcategories': subcategories}
    return render(request, 'subcategories.html', context)


def posts_with_audio(request, category_slug, subcategory_slug):  # zmiana na category_slug
    subcategory = get_object_or_404(Subcategory, slug=subcategory_slug)
    posts = Post.objects.filter(subcategory=subcategory).exclude(audio_file=None)
    context = {'posts': posts}
    return render(request, 'posts_with_audio.html', context)


