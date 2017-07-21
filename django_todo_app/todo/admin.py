from django.contrib import admin

from .models import Todo, Comment


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = { 'slug': ('title',) }


class CommentAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Todo, TodoAdmin)
admin.site.register(Comment, CommentAdmin)
