from django import forms
from django.utils.translation import ugettext_lazy as _
from base.constant import PREGUNTA1, PREGUNTA2_1, PREGUNTA2_2, PREGUNTA3, SI_NO, PREGUNTA4
from .models import Encuesta1

class Encuesta1Form(forms.ModelForm):
    pregunta1 = forms.ChoiceField(
        label=_("1.- ¿Para qué cree Ud. que sería útil una Asamblea Constituyente?"),
        choices=(('',_('Seleccione una de las opciones')),)+PREGUNTA1,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:100%;',
                'title': _("Seleccione una de las opciones"),
            }
        ),
        required=False
    )

    pregunta2 = forms.ChoiceField(
        label=_("2.- ¿Apoya usted la Convocatoria a la Asamblea Nacional Constituyente hecha por Nicolas Maduro?"),
        choices=(('',_('Seleccione una de las opciones')),)+SI_NO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:100%;',
                'title': _("Seleccione una de las opciones"), 'onchange': "__pregunta2(this.value);"
            }
        ),
        required=False
    )

    pregunta2_1 = forms.ChoiceField(
        label=_("2.1.- Indique la Razón"),
        choices=(('',_('Seleccione una de las opciones')),)+PREGUNTA2_1,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:100%;',
                'title': _("Seleccione una de las opciones"),
            }
        ),
        required=False
    )

    pregunta2_2 = forms.ChoiceField(
        label=_("2.2.- Indique la Razón"),
        choices=(('',_('Seleccione una de las opciones')),)+PREGUNTA2_2,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:100%;',
                'title': _("Seleccione una de las opciones"),
            }
        ),
        required=False
    )

    pregunta3 = forms.ChoiceField(
        label=_("3.- Si las elecciones a la Presidencia de la República fueran hoy, ¿por quien votaría usted?"),
        choices=(('',_('Seleccione una de las opciones')),)+PREGUNTA3,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:100%;',
                'title': _("Seleccione una de las opciones"),
            }
        ),
        required=False
    )

    pregunta4 = forms.ChoiceField(
        label=_(" En el ambito terrritorial, ¿cual candidato apoya usted?"),
        choices=(('',_('Seleccione una de las opciones')),)+PREGUNTA4,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:100%;',
                'title': _("Seleccione una de las opciones"),
            }
        ),
        required=False
    )

    ## Número telefónico de contacto con el usuario
    telefono = forms.CharField(
        label=_("Teléfono:"),
        max_length=18,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'placeholder': '(+058)-000-0000000',
                'data-rule-required': 'true', 'data-toggle': 'tooltip',
                'title': _("Indique el número telefónico de contacto"), 'data-mask': '(+000)-000-0000000',
                'value':'058'
            }
        ),
        help_text=_("(+058)-416-0000000")
    )

    class Meta:
        model = Encuesta1
        exclude = ['user']
