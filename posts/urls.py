from django.urls import path
from posts.views import AddPostCreateView, EditPostUpdateView, DeletePostDeleteView, DetailsPostView

urlpatterns = [
    # path('add/', add_post, name='add_post'),
    path('add/', AddPostCreateView.as_view(), name='add_post'),
    # path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('edit/<int:post_id>/', EditPostUpdateView.as_view(), name='edit_post'),
    # path('delete/<int:post_id>/', delete_post, name='delete_post')
    path('delete/<int:post_id>/', DeletePostDeleteView.as_view(), name='delete_post'),
    path('details/<int:pk>/', DetailsPostView.as_view(), name='details_post')
]
