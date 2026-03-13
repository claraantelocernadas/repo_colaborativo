#función 1: registrar_habitos()

actividades = []

def registrar_habitos():
    pregunta = input("Quiere ingresar una actividad?" )

    while pregunta == "si":
        actividad = input("Ingresa una activadad: ")
        actividades.append(actividad)


