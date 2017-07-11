from django.conf.urls import url
from django.contrib.auth.views import login, logout, password_change, password_change_done

urlpatterns = [
    url(r'^login$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout$', logout, name='logout'),
    url(r'^cambiar-clave$', password_change, {'template_name': 'password_change_form.html'}, name='password_change'),
    url(r'^cambiar-clave-hecho$', password_change_done, {'template_name': 'password_change_done.html'}, name='password_change_done'),
]

