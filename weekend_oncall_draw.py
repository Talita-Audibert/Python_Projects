from datetime import timedelta, date
import requests

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

#def get_holiday(date):
#    url = f'https://api.calendario.com.br/?json=true&token=[seu-token]&ano={date.year}&estado=RS&cidade=Porto_Alegre'
#    feriados = requests.
 
  

start_dt = date(2022,1,1)
end_dt = date(2022,12,31)

sorteado = ['Pessoa 1', 'Pessoa 2', 'Pessoa 3']
st = len(sorteado)

for dt in daterange(start_dt, end_dt):
    
    if dt.weekday() == 5:
        sun = dt+timedelta(1)
        if dt.month == sun.month:
            print(dt.strftime(f"%d & {sun.day} %B - " + sorteado[st-1]))
        else:
            print(("{0:%d} {0:%B}").format(dt) + " & " + ("{0:%d} {0:%B} - ").format(sun) + sorteado[st-1])
    st -=1
    if st == 0:
        st = len(sorteado)
