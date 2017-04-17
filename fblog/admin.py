#encoding: utf-8
from django.contrib import admin

# Register your models here.
from models import Article,Category,Tag,Fk_Category

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','created_time')

class Fk_CategoryAdmin(admin.ModelAdmin):
    list_display=('name','create_time')

admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Fk_Category,Fk_CategoryAdmin)
