from django.conf.urls import url
from . import views
from django.contrib import admin
from .models import Editor,Article,tags
from django.conf import settings
from django.conf.urls.static import static
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

# admin.site.register(Editor)
# admin.site.register(Article,ArticleAdmin)
# admin.site.register(tags)

urlpatterns=[
    url(r'^$',views.news_today,name='newsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^article/(\d+)',views.article,name ='article')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)