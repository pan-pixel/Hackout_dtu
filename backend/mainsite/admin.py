from django.contrib import admin

from .models import News_analysis

# Register your models here.

# class News_analysis_Pro(admin.ModelAdmin):
#     list_display = ('company','headline')


admin.site.register(News_analysis)
