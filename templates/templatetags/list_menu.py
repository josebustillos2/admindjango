import re

from django.contrib.admin.views.main import PAGE_VAR
from django.template import Library
from django.utils.html import format_html
from django.utils.safestring import mark_safe

register = Library()



@register.simple_tag
def get_name_app(request):
    route = request.resolver_match.route
    search = re.search(r'\(\?P<app_label>', route)
    name_app=''
    if not search:
        name_app = route.split('/')[1]
    else:
        match = re.search(r'\(\?P<app_label>(\w+)', route)
        if match:
            name_app = match.group(1)
    return name_app



@register.simple_tag
def get_name_model(request):
    route = request.resolver_match.route
    search = re.search(r'\(\?P<app_label>', route)
    name_app=''
    if not search:
        try:
            name_app = route.split('/')[2]
        except IndexError:
            name_app=''
    return name_app

