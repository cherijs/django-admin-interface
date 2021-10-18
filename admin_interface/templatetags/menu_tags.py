import logging

import django
from django import template
from django.conf import settings
from django.contrib.admin import AdminSite
from django.http import HttpRequest
from django.utils.module_loading import import_string

from admin_interface.menu import MenuManager

if django.VERSION < (1, 10):
    from django.core.urlresolvers import reverse, resolve
else:
    from django.urls import reverse, resolve

register = template.Library()

if django.VERSION < (1, 9):
    simple_tag = register.assignment_tag
else:
    simple_tag = register.simple_tag


@simple_tag(takes_context=True)
def get_menu(context, request):
    """
    :param context:
    :type request: WSGIRequest
    """
    if not isinstance(request, HttpRequest):
        return None

    is_enabled = False

    if hasattr(settings, "ADMIN_INTERFACE_ENABLE_MENU"):
        is_enabled = settings.ADMIN_INTERFACE_ENABLE_MENU

    if not is_enabled:
        return

    # Django 1.9+
    available_apps = context.get('available_apps')
    if not available_apps:

        # Django 1.8 on app index only
        available_apps = context.get('app_list')

        # Django 1.8 on rest of the pages
        if not available_apps:
            try:
                from django.contrib import admin
                template_response = get_admin_site(request.current_app).index(request)
                available_apps = template_response.context_data['app_list']
            except Exception:
                pass

    if not available_apps:
        logging.warn('Django was unable to retrieve apps list for menu.')

    if hasattr(settings, "ADMIN_INTERFACE_MENU"):
        menu_class = import_string(settings.ADMIN_INTERFACE_MENU)
        return menu_class(available_apps, context, request)
    return MenuManager(available_apps, context, request)


def get_admin_site(current_app):
    """
    Method tries to get actual admin.site class, if any custom admin sites
    were used. Couldn't find any other references to actual class other than
    in func_closer dict in index() func returned by resolver.
    """
    try:
        resolver_match = resolve(reverse('%s:index' % current_app))
        # Django 1.9 exposes AdminSite instance directly on view function
        if hasattr(resolver_match.func, 'admin_site'):
            return resolver_match.func.admin_site

        for func_closure in resolver_match.func.__closure__:
            if isinstance(func_closure.cell_contents, AdminSite):
                return func_closure.cell_contents
    except:
        pass
    from django.contrib import admin
    return admin.site


@simple_tag
def color_variant(hex_color, brightness_offset=1):
    """ takes a color like #87c95f and produces a lighter or darker variant """
    if len(hex_color) != 7:
        raise Exception("Passed %s into color_variant(), needs to be in #87c95f format." % hex_color)
    rgb_hex = [hex_color[x:x + 2] for x in [1, 3, 5]]
    new_rgb_int = [int(hex_value, 16) + brightness_offset for hex_value in rgb_hex]
    new_rgb_int = [min([255, max([0, i])]) for i in new_rgb_int]  # make sure new values are between 0 and 255
    # hex() produces "0x88", we want just "88"
    return "#" + "".join([hex(i)[2:] for i in new_rgb_int])
