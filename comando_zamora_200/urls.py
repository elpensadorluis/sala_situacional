from django.conf.urls import url
from .views import PersonaCreate, FrenteList
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(FrenteList.as_view()), name='frente_lista'),
    url(r'^registro$', login_required(PersonaCreate.as_view()), name='persona_registro'),
]
