import hashlib

class HASH:
  ##Función que genera el hash
  def generarHash(h):
    digest = h.hexdigest()
    return digest

##Menu
def menu():
  print("Bienvenido al menu de hash, tenemos las opciones: ")
  print("1. Encriptar por SHA256")
  print("2. Encriptar por SHA512")
  print("3. Salir")
  print("Escoja el algoritmo a usar: ")
  opcion = int(input())

  while opcion >=1 and opcion <3:
    print("Ingrese los datos que desea codificar: ")
    datos = input()
    algoritmo  =  ""
    datoHash = bytes(datos, 'utf-8')

    ##Hace la encriptacion de hash 256
    if opcion == 1:
        algoritmo = "sha256"   
        h = hashlib.sha256(datoHash)
        hash256 = HASH.generarHash(h)
        print("El resultado de la encriptacion en sha256 es: ",hash256)
        print()
        return menu()

   ##Hace la encriptacion de hash 512
    elif opcion == 2:
      algoritmo = "sha512"
      h = hashlib.sha512(datoHash)
      hash512 = HASH.generarHash(h)
      print("El resultado de la encriptacion en sha512 es: ",hash512)
      print()
      return menu()

    ##Sale del menu
    else:
      print("Gracias por haber usado el programa")
      exit()

menu()
