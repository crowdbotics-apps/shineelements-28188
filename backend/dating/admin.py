from django.contrib import admin
from .models import Setting, Like, UserPhoto, Match, Dislike, Inbox, Profile

admin.site.register(Like)
admin.site.register(UserPhoto)
admin.site.register(Dislike)
admin.site.register(Setting)
admin.site.register(Match)
admin.site.register(Inbox)
admin.site.register(Profile)

# Register your models here.
