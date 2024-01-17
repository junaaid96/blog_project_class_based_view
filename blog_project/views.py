from django.shortcuts import render
from posts.models import Post
from categories.models import Category

# category_slug is None by default. If the user doesn't select a category, then all posts will be displayed.


def home(request, category_slug=None):
    posts = Post.objects.all()

    if category_slug is not None:
        # using the double underscore to access the slug field of the category model.
        # posts = Post.objects.filter(categories__slug=category_slug)
        # another way to do this is to use the get() method. slug is the field name in the Category model. category_slug is the variable passed in the function.
        category = Category.objects.get(slug=category_slug)
        posts = Post.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'home.html', {'posts': posts, 'categories': categories})
