from pydoc import describe
from sqlite3 import apilevel
from jinja2 import TemplateRuntimeError
import requests
from tables import Description


API_KEY = "61fac0a9afb44774c7783d9f9f2409ba"
cidade = input("Digite a cidade que você deseja saber como está o tempo: ")

link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
#print(requisicao)
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] -273,15

def tempMaior28():
    print(descricao, "com temperatura acima de 28 "f'{temperatura}°C')
def tempMenor28():
    print(descricao, "com temperatura "f'{temperatura}°')

if temperatura[0] > 28:
    tempMaior28()

else:
    tempMenor28()

    

