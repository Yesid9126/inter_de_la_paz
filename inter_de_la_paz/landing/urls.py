# Django
from django.urls import path

# Views
from inter_de_la_paz.landing import views as landing_views

app_name = "landing"
urlpatterns = [
    path(route="", view=landing_views.LandingView.as_view(), name='landing')
]
