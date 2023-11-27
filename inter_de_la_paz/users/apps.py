from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "inter_de_la_paz.users"
    verbose_name = _("Users")
