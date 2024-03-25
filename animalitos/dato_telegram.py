
from datetime import datetime, timedelta
from home.extraccion_tuazar import *
import requests





def bot_send_text(dato1, dato2):
  bot_token = '5824717648:AAFYTk6i8hZCBU030dwuooEJuL0pHkgR9og'
  bot_chatID = '1174164422'
  dato1=str(dato1)
  dato2=str(dato2)
  nombre_dato2=capture_nombre(dato2)
  nombre_dato1=capture_nombre(dato1)
  actual = datetime.now()
  tomorrow = actual + timedelta(days=1)
  fecha_str = tomorrow.strftime('%d/%m/%Y')
  send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' +' ' + 'Fecha '+ fecha_str +'  ' + ' Dato (1)= '+' '+ nombre_dato1+ '('+ dato1+')' +' '+ '  Dato (2)= '+' '+ nombre_dato2 + '('+ dato2+')' 
  response = requests.get(send_text)
  return response


datos=datos_excel()
dato1=datos[0]
dato2=datos[1] 
bot_send_text(dato1,dato2)