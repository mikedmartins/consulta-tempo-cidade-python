from shutil import register_unpack_format
import string

string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 0123456789
string.punctuation # <=>?@[\]^_`{|}~.

from random import choice
import string

while True:
    tamanho = int(input ('Digite a quantidade de caracteres da senha: '))

    print('Digite 1 somente letras minusculas')
    print('Digite 2 para letras minuscolas e maiusculas')
    print('Digite 3 para letras e números')
    print('Digite 4 para letras, números e caracteres')
    tipo = int(input())
    valores = ()
    if tipo == 1:
        valores = string.ascii_lowercase
        break
    if tipo == 2:
        valores = string.ascii_lowercase + string.ascii_uppercase
        break
    if tipo == 3:
        valores = string.ascii_lowercase + string.ascii_uppercase + string.digits
        break
    if tipo == 4:
        valores = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        break
    else:
        print('Digite alguma alternativa solicitada')  

senha = ''
for i in range(tamanho):
    senha += choice(valores)

print(senha)