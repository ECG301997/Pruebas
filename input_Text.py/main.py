import re
def incoming_message(message):
    mensaje = message.upper()
    lista  = re.split(r' ',mensaje)
    resultado = {}
    for n in lista:
        if n in resultado:
            resultado[n] += 1
        else:
            resultado[n] = 1
    return resultado      
mensaje = "Hi how are things? How are you? Are you a developer? I am also a developer"
print(incoming_message(mensaje))