from django.contrib import admin

from .models import Category
from .models import Article

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display =('name','description','created_at')            

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'price','stock','image','created_at')
    
    
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
