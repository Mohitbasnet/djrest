from django.contrib import admin

# Register your models here.
from . models import Question,Answer
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "body",
    )
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)