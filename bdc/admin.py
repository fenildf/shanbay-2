# encoding: utf-8
from django.contrib import admin

from .models import Word


class WordAdmin(admin.ModelAdmin):
    fields = ['name', 'pronunciation', 'definition']
    list_display = ('name_capitalized',)

    def name_capitalized(self, obj):
        return obj.name.capitalize()
    name_capitalized.short_description = '大写'

admin.site.register(Word, WordAdmin)
