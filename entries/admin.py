from entries.models import Ad
from django.contrib import admin

class AdAdmin(admin.ModelAdmin):
	fields = ['type', 'title', 'description', 'price', 'date', 'image_url']

admin.site.register(Ad, AdAdmin)
