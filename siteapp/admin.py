from django.contrib import admin
from siteapp.models import Setting, Link, MenuItem


class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')


class LinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'page_template_name', 'page_name')


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'position', 'link')

admin.site.register(Setting, SettingAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
