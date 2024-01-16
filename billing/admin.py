from django.apps import apps
from django.contrib import admin
from django.utils.translation import gettext_lazy


class TechFactSite(admin.AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = gettext_lazy("TECHFACT")

    # Text to put in each page's <h1>.
    site_header = gettext_lazy("TECHFACT")

    # Text to put at the top of the admin index page.
    index_title = gettext_lazy("TECHFACT")

    def _build_app_dict(self, request, label=None):
        app_dict = super()._build_app_dict(request, label)
        for app_label, app_config in app_dict.items():
            if  'name' in app_config:
                app_dict[app_label]['icon'] = app_label
        return app_dict
class BillingModelAdmin(admin.ModelAdmin):
    cl_local_storage = None

    # CUSTOM FIELDS
    def get_site(self, obj):
        return obj.establishment.site.name

    """"
        Overwrite perms import
    """


TechFactSite = TechFactSite()
