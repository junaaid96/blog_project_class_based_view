from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # one post can have many categories and one category can have many posts. So we use ManyToManyField.
    category = models.ManyToManyField(Category)
    # one post can have only one author and one author can have many posts. So we use ForeignKey.
    # on_delete=models.CASCADE means if we delete an author, all the posts of that author will be deleted.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # if we want to keep the posts of an author even if we delete the author, we can use on_delete=models.SET_NULL
    # author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title