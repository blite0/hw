from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(CommentPost)
admin.site.register(LikeComment)
admin.site.register(DisslikeComment)
admin.site.register(LikePost)
admin.site.register(DisslikePost)