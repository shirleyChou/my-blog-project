from django.contrib import admin
from models import Post

# Register your models here.
"""
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')
"""

class PostAdmin(admin.ModelAdmin):
    #list_display = ('title', 'publisher', 'publication_date')
    # filter by date
    # list_filter = ('publication_date',)
    # select date from year, month, day: accept string rather than tuple
    date_hierarchy = 'update_time'
    ordering = ('update_time',)
    # define the sequence of fields in a specific book, it can escape some fields that don't want to be changed
    # fields = ('title', 'authors', 'publisher')
    # for manytomany
    #filter_horizontal = ('authors',)
    # for foreign key like publisher
    #raw_id_fields = ('publisher',)

#admin.site.register(Publisher)
#admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)

