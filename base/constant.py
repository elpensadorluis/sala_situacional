from django.utils.translation import ugettext_lazy as _

## Mensaje de error para peticiones AJAX
MSG_NOT_AJAX = _("No se puede procesar la petición. "
                 "Verifique que posea las opciones javascript habilitadas e intente nuevamente.")

TIPO_FRENTE = (
    ("JC",_("Jefe del Comando Zamora 200")),
    ("GC",_("Gobierno de Calle Constituyente")),
    ("OE",_("Organización y Estructura de la Maquinaria Electoral")),
    ("EP",_("Estrategia y Propaganda")),
    ("MP",_("Movilización Permanente")),
    ("FM",_("Frente de Movimientos Sociales Constituyentes")),
)

SHORT_NACIONALIDAD = (
    ("V", "V"), ("E", "E")
)

PREGUNTA1 = (
    ("a",_("Para generar nuevos derechos y deberes de los ciudadanos o mejorar los existentes")),
    ("b",_("Para mejorar los servicios públicos")),
    ("c",_("Para que el gobierno haga mejor su trabajo")),
    ("d",_("Para que la oposición haga mejor su trabajo")),
)

SI_NO = (
    ("S",_("Si")),
    ("N",_("No")),
)

PREGUNTA2_1 = (
    ("a",_("Unico mecanismo para lograr la paz")),
    ("b",_("Solución a los problemas económicos")),
    ("c",_("Eliminar la inpunidad")),
    ("d",_("Gantizará los derechos sociales")),
)

PREGUNTA2_2 = (
    ("a",_("Es Ilegal")),
    ("b",_("No resuelve los problemas del país")),
    ("c",_("Temor por su trabajo")),
    ("d",_("Temor por  su vida")),
    ("e",_("Representa una patraña del gobierno")),
)

PREGUNTA3 = (
    ("a",_("Candidato del Oficialismo")),
    ("b",_("Candidato de la Oposición")),
    ("c",_("Candidato Independiente")),
    ("d",_("No votaría")),
)

PREGUNTA4 = (
    ("1",_("1.- Jehyson Jose Guzman Araque / Simon Pablo Figueroa")),
    ("2",_("2.- Agustin Alexis Alvarez Tovar / Lorenza Ullan Severino")),
    ("3",_("3.- Betty Carolina PeÑa Lopez")),
    ("4",_("4.- Elias Rafael Sanchez Verde / Juan Carlos Lenzo")),
    ("5",_("5.- Enrique Antonio Plata Ramirez / Teresa De Jesus Mora ")),
    ("6",_("6.- Nelsy Carolina Rivera Quinchoa")),
    ("7",_("7.- Luis Carlos Perales Araque")),
    ("8",_("8.- Johnny Rafael Andrade Barreto")),
    ("9",_("9.- Jorge David Sandoval Rujano")),
    ("10",_("10.- Gracian Claret Rondon Dezeo")),
    ("11",_("11.- Greny Rosana Uzcategui Lacruz")),
    ("12",_("12.- Hector Ramon Rojas Pernia")),
    ("13",_("13.- Wilmer Arquimedes Iglesias Pino / Ramon David Fajardo Guanipa")),
    ("14",_("14.- Alirio Jose Liscano ")),
    ("15",_("15.- Jose Rafael Luna ")),
)
