from django.contrib import admin

from todo.models import Tag, Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "created_datetime", "deadline_datetime", "is_done"]
    list_filter = ["tags"]
    search_fields = ["content"]


admin.site.register(Tag)
admin.site.register(Task, TaskAdmin)
