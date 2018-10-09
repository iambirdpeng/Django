from django.contrib import admin

from models import *


class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    extra = 3


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'btitle', 'bpub_date']
    search_fields = ['btitle']
    inlines = [HeroInfoInline]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'hname', 'gender', 'hcontent', 'hbook']

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)

