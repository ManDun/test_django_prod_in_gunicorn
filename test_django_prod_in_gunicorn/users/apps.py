from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "test_django_prod_in_gunicorn.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import test_django_prod_in_gunicorn.users.signals  # noqa F401
        except ImportError:
            pass
