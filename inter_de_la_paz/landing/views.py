# Django
from django.views.generic import TemplateView


class LandingView(TemplateView):
    """Landing view."""
    template_name = 'landing/index.html'

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
