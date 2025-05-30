# Django
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from inter_de_la_paz.users.managers import UserManager


class User(AbstractUser):
    """
    Default custom user model for inter_de_la_paz.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    email = EmailField(_("email address"), unique=True)
    username = None  # type: ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})


class Profile(models.Model):
    """Profile model."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    eps = models.CharField(max_length=255)
    from_team = models.CharField(max_length=255)
    age = models.PositiveIntegerField()

    def __str__(self):
        """Return users name."""
        return f"Profile for {self.user.name}"

    class Meta:
        """Meta class."""

        verbose_name = "Perfil de usuario"
        verbose_name_plural = "Perfiles de usuarios"
