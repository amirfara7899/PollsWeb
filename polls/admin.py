from django.contrib import admin
from .models import Question, Choice


# Register your models here.

class QuestoinAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'votes', 'question')


admin.site.register(Question, QuestoinAdmin)
admin.site.register(Choice, ChoiceAdmin)
