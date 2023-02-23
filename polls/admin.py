from django.contrib import admin

from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  { 'fields': ['question_text', 'created_by'] }),
        ('Date information',    { 'fields': ['published_at'] })
    ]

    inlines = [ChoiceInline]

    list_display = ('question_text', 'published_at', 'was_published_recently')

    list_filter = ['published_at']

admin.site.register(Question, QuestionAdmin)