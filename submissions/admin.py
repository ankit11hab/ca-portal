from django.contrib import admin
from .models import POC, POCBulk,Submission,Idea,Media
# Register your models here.

class POCAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_verified')

class POCBulkAdmin(admin.ModelAdmin):
    list_display = ('csv_file', 'is_verified')

class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_verified')

admin.site.register(POC, POCAdmin)
admin.site.register(POCBulk, POCBulkAdmin)
admin.site.register(Idea, IdeaAdmin)
admin.site.register(Media)
