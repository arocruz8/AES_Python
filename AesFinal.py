##Algoritmo AES 

##Librerias
from Cryptodome.Cipher import AES
from secrets import token_bytes

##Llave de 16 bytes de tamaño
llave = token_bytes(16)

##Función que encripta
def encriptar(msg):
    cipher = AES.new(llave, AES.MODE_EAX)
    nonce = cipher .nonce
    ##se aplica el algoritmo de encriptacion
    textocifrado, tag = cipher .encrypt_and_digest(msg.encode('ascii'))
    return nonce, textocifrado, tag

##Función que desencriptado
def desencriptar(nonce, textocifrado, tag):
    cipher   = AES.new(llave, AES.MODE_EAX, nonce=nonce)
    ##aplica el algoritmo para desencriptar el texto cifrado
    textInicial =  cipher .decrypt(textocifrado)
    try:
        cipher.verify(tag)
        ##retorna el algoritmo desencriptado
        return textInicial.decode('ascii')
    except:
        return False

##Ejecución del código
nonce, textocifrado, tag = encriptar(input('Ingrese el mensaje que desea encriptar: '))
textInicial = desencriptar(nonce, textocifrado, tag)
print(f'Texto cifrado: {textocifrado}')
if not textInicial:
    print('El mensaje fue corrupto')
else:
    print(f'Texto descencriptado: {textInicial}')
