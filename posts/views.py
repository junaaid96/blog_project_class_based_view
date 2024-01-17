from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms, models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView

# @login_required
# def add_post(request):
#     # user sending post request to add post
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request. (capturing the data from post request.)
#         post_form = forms.PostForm(request.POST)
#         # check whether it's valid.
#         if post_form.is_valid():
#             post_form.instance.author = request.user
#             # process the data in form.cleaned_data as required. (saving the data to the database.)
#             post_form.save()
#             # redirect to a new URL
#             return redirect('home')
#     else:
#         # user sending get request to add post (displaying the form.)
#         post_form = forms.PostForm()
#     # render the template depending on the request. (displaying the form.)
#     return render(request, 'add_post.html', {'form': post_form})

# Class based view


@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    # reverse_lazy is used because we are using class based view. its a class based url redirect.
    success_url = reverse_lazy('home')
    # form is created from the form_class. so we are overriding the form_valid method of the parent class.

    def form_valid(self, form):
        form.instance.author = self.request.user
        # super() is used to call the parent class method. so we are overriding the parent class method. means we let the parent class method to do its work and we are adding some extra work to it.
        return super().form_valid(form)


# @login_required
# def edit_post(request, post_id):
#     # get the post from the database
#     post = forms.Post.objects.get(pk=post_id)
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request.
#         # here instance means the form is pre-populated with the data from the database.
#         # here request.POST and instance=post both are required. so that if user doesn't change anything, it will save the previous data.
#         post_form = forms.PostForm(request.POST, instance=post)
#         if post_form.is_valid():
#             post_form.instance.author = request.user
#             post_form.save()
#             return redirect('home')
#     else:
#         # user sending get request to edit post (displaying the form with pre-populated data.)
#         post_form = forms.PostForm(instance=post)
#     return render(request, 'add_post.html', {'form': post_form})

@method_decorator(login_required, name='dispatch')
class EditPostUpdateView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'post_id'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# @login_required
# def delete_post(request, post_id):
#     # we can use models.Post.objects.get also both are same here.
#     post = forms.Post.objects.get(pk=post_id)
#     post.delete()
#     return redirect('home')

@method_decorator(login_required, name='dispatch')
class DeletePostDeleteView(DeleteView):
    model = models.Post
    template_name = 'delete_post.html'
    pk_url_kwarg = 'post_id'
    success_url = reverse_lazy('profile')
