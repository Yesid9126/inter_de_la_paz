# Django
from django.views.generic import TemplateView


class LandingView(TemplateView):
    """Landing view."""
    template_name = 'landing/index.html'
