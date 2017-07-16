from django.conf.urls import url
from .views import Encuesta1Create, Encuesta1List
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(Encuesta1List.as_view()), name='encuesta1_lista'),
    url(r'^registro$', login_required(Encuesta1Create.as_view()), name='encuesta1_registro'),
]
