
def analizar_habitos (lista):
     resultado = {} 
     
     for actividad in lista:
         if actividad in resultado:
             resultado [actividad]+=1 
         else:
            resultado [actividad] = 1
            
     return resultado 