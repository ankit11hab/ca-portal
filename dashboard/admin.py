from django.contrib import admin
from .models import Notifications, ShareablePost,Promotions
# Register your models here.
admin.site.register(ShareablePost)
admin.site.register(Notifications)
admin.site.register(Promotions)