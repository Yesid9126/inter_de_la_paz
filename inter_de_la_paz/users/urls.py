# Django
from django.urls import path

# Views
from inter_de_la_paz.users import views as users_views

app_name = "users"
urlpatterns = [
    #path(route="", view=users_views.LandingViewUSers.as_view(), name='users')
]
