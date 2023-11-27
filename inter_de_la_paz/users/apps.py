from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "inter_de_la_paz.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import inter_de_la_paz.users.signals  # noqa: F401
        except ImportError:
            pass
