from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(models.Category)

# to customize admin panel we need to create a class and inherit it from admin.ModelAdmin class.
# then we need to register the model with the class.


class CategoryAdmin(admin.ModelAdmin):
    # list display is used to display the fields in the admin panel. (by default it will display the name of the model.)
    list_display = ('name', 'slug')
    # prepopulated_fields is used to pre-populate the slug field with the name field. (it will automatically generate the slug field.)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.Category, CategoryAdmin)
