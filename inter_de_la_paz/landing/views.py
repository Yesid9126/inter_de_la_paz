# Django
from django.http import JsonResponse
from django.views.generic import TemplateView

# Models
from inter_de_la_paz.users.models import Profile, User


class LandingView(TemplateView):
    """Landing view."""

    template_name = "landing/index.html"

    def post(self, request, *args, **kwargs):
        """Create contact."""
        data = request.POST
        name = data.get("name")
        phone = data.get("phone")
        email = data.get("email")
        eps = data.get("eps")
        age = data.get("age")
        from_team = data.get("from-team")
        user = User.objects.create(
            name=name,
            email=email,
        )
        Profile.objects.create(user=user, phone_number=phone, eps=eps, age=age, from_team=from_team)
        response_data = {"message": "Registro exitoso. Pronto nos comunicaremos contigo para darte indicaciones."}
        return JsonResponse(response_data)
