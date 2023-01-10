from django.contrib import admin
from .models import Question, Choice
from django.utils import timezone

# Register your models here.
# admin.site.register(Question)
# admin.site.register(Choice)


# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields=['pub_date','question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]

    list_display = ['question_text', 'pub_date', 'was_published_recently']
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
