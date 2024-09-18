from django.contrib import admin
from newspaper.models import Newsletter, Post, Category, Tag, Contact, UserProfile, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Newsletter)


# admin.site.register([Post,Category,Tag])



class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)
