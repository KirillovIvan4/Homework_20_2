from django.contrib import admin

from editor.models import Publications


# Register your models here.

@admin.register(Publications)
class PublicationsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'views_count',)
