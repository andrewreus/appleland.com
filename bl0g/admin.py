from django.contrib import admin
from .models import Mod, Categories


class ModsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'characteristics', 'image')
    list_display_links = ('name', )
    search_fields = ('name', )

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name', )
    search_fields = ('name', )


admin.site.register(Mod, ModsAdmin)
admin.site.register(Categories)
