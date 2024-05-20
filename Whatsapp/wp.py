import pyautogui as pg
import webbrowser as web
import time
import pandas as pd

data = pd.read_csv("datos.csv")
data_dict = data.to_dict('list')
celulares = data_dict['celular']
mensajes = data_dict['mensaje']
nombres = data_dict['nombre']
combo = zip(celulares,mensajes,nombres)
first = True
for celular,mensaje,nombres in combo:
    #time.sleep(8)
    web.open("https://web.whatsapp.com/send?phone="+celular+"&text="+"Hola buenas tardes "+nombres+" "+mensaje)
    if first:
        #time.sleep(8)
        first=False
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(10)
    #time.sleep(8)
    pg.press('enter')
    #time.sleep(6)
    time.sleep(4)
    pg.hotkey('ctrl','w')    