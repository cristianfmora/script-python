import pywhatkit 

try: 

  # Enviamos el mensaje
  pywhatkit.sendwhatmsg("+57numeroTelefono",  
                        "Mensaje De Prueba",
                        21,18) 

  print("Mensaje Enviado") 
except: 
  print("Ocurrio Un Error")