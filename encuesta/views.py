from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Encuesta1
from .forms import Encuesta1Form
from django.contrib.auth.models import User

# Create your views here.

class Encuesta1List(ListView):
    model = Encuesta1
    template_name = "encuesta1.lista.html"

    def get_queryset(self):
        queryset = Encuesta1.objects.filter(user__username=self.request.user)
        return queryset

class Encuesta1Create(CreateView):
    model = Encuesta1
    form_class = Encuesta1Form
    template_name = "encuesta1.registro.html"
    success_url = reverse_lazy('encuesta1_lista')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        user = User.objects.get(username=self.request.user.username)
        self.object.pregunta1 = form.cleaned_data['pregunta1']
        self.object.pregunta2 = form.cleaned_data['pregunta2']
        self.object.pregunta2_1 = form.cleaned_data['pregunta2_1']
        self.object.pregunta2_2 = form.cleaned_data['pregunta2_2']
        self.object.pregunta3 = form.cleaned_data['pregunta3']
        self.object.pregunta4 = form.cleaned_data['pregunta4']
        self.object.telefono = form.cleaned_data['telefono']
        self.object.user = user
        self.object.save()
        return super(Encuesta1Create, self).form_valid(form)

    def form_invalid(self, form):
        return super(Encuesta1Create, self).form_invalid(form)
