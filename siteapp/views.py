# -*- coding: cp1251 -*-
from django.shortcuts import render
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from models import Setting, MenuItem, Link
import datetime


class SiteEngine(object):
    def __init__(self):
        pass

    @staticmethod
    def get_settings():
        settings_dict = {'currentYear': datetime.datetime.now().year}
        settings = Setting.objects.all()
        for setting in settings:
            settings_dict.update({setting.name: setting.value})
        return settings_dict

    @staticmethod
    def get_menu_items():
        menu_items = list()
        for menu_item in MenuItem.objects.all().order_by('position'):
            if menu_item.parent is None:
                menu_item.items = MenuItem.objects.filter(parent=menu_item).order_by('position')
                menu_items.append(menu_item)
        return menu_items

    @staticmethod
    def render(request, template_name, context=None):
        site_context = dict()
        site_context.update(SiteEngine.get_settings())
        site_context.update({'menu_items': SiteEngine.get_menu_items()})
        site_context.update({'current_url': request.get_full_path()})
        if context:
            site_context.update(context)
        return render(request, template_name, site_context)


def default(request):
    return SiteEngine.render(request, 'siteapp/default.html')


def pages_handler(request):
    context = dict()

    try:
        link_object = Link.objects.get(url=request.get_full_path())
        template_name = "siteapp/pages/%s" % link_object.page_template_name
        if link_object.page_name:
            context.update({'page_name': link_object.page_name})
    except Link.DoesNotExist:
        raise Http404

    menu_item = MenuItem.objects.filter(link=link_object).order_by("position").first()
    if menu_item:
        breadcrumbs = list()
        item = menu_item.parent
        while item is not None:
            breadcrumbs.append(item)
            item = item.parent
        breadcrumbs.reverse()
        context.update({'breadcrumbs': breadcrumbs})
        if not 'page_name' in context:
            context.update({'page_name': menu_item.name})

    return SiteEngine.render(request, template_name, context=context)
