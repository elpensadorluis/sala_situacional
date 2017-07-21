from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from base.constant import PREGUNTA1, SI_NO, PREGUNTA2_1, PREGUNTA2_2, PREGUNTA3, PREGUNTA4
from django.contrib.auth.models import User

# Create your models here.

class Encuesta1(models.Model):
    pregunta1 = models.CharField(max_length=1, choices=PREGUNTA1)

    pregunta2 = models.CharField(max_length=1, choices=SI_NO)

    pregunta2_1 = models.CharField(max_length=1, choices=PREGUNTA2_1)

    pregunta2_2 = models.CharField(max_length=1, choices=PREGUNTA2_2)

    pregunta3 = models.CharField(max_length=1, choices=PREGUNTA3)

    telefono = models.CharField(
        max_length=18, help_text=_("Número telefónico de contacto con la persona"),
        validators=[
            validators.RegexValidator(
                r'^\(\+\d{3}\)-\d{3}-\d{7}$',
                _("Número telefónico inválido. Solo se permiten números y los símbolos: '(', ')', '-', '+'")
            ),
        ]
    )

    pregunta4 = models.CharField(max_length=1, choices=PREGUNTA4)

    user = models.ForeignKey(User)
