def registrar_habitos():
    '''
    Guarda en una lista las actividades que se le piden al usuario 
    
    Returns
    -------
    list: una lista de todas las actividades que haya ingresado el usuario
    '''
   
    pregunta = input("Quiere ingresar una actividad?" )
    actividades = []
    while pregunta == "si":
        actividad = input("Ingresa una activadad: ")
        actividades.append(actividad)


def analizar_habitos(lista): 
    '''
    Cuenta cuantas veces aparece cada actividad ingresada por el usuario

    Parameters
    ----------
    lista : list
        una lista de todas las actividades ingresadas por el usuario

    Returns
    -------
    diccionario
        diccionario contador de frecuencias de cuantas veces ingresa el usuario esa actividad

    '''
    
    resultado = {} 
    
    for actividad in lista:
        if actividad in resultado:
            resultado [actividad]+=1 
        else:
           resultado [actividad] = 1
           
    return resultado 
