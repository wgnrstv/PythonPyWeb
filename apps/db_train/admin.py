from django.contrib import admin
from .models import Author, AuthorProfile, Entry, Tag

admin.site.register(Author)
admin.site.register(AuthorProfile)
admin.site.register(Entry)
admin.site.register(Tag)
