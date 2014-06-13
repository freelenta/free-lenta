from django.contrib import admin
from news_site.models import Article

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date', 'category')
	list_filter = ['pub_date']
	search_fields = ['main_text']

admin.site.register(Article, ArticleAdmin)
