nombre = input("Ingrese su nombre: ")

from datetime import datetime

hora_actual = datetime.now().hour

if hora_actual < 12:
    saludo = "Buenos días"
elif hora_actual < 20:
    saludo = "Buenas tardes"
else:
    saludo = "Buenas noches"

print(f"{saludo}, {nombre}!")