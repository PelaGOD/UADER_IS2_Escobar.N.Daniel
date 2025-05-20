# Compiled at: 2022-06-14 16:15:55
import sys
from SingletonGetJson import SingletonGetJson

version = "{0.1}"
fileName = "sitedata"
arg = sys.argv

if len(arg) == 1:
    s = SingletonGetJson()

    tk = input("Ingrese el token: ")

    try:
        clave = s.getToken(tk)
        print (version + " " + clave)
    except:
        print ("ups, hubo un error al intentar mostrar el token")

elif arg[1] in ["-h", "--help"]:
    print ("Ejemplo de uso")
    print ("Ingrese el token: token1")
    print (version + "XXXX-XXXX-XXXX-XXXX")

    print ("")
    print ("El archivo json 'sitedata.json' debera encontrarse en la misma carpeta de este mismo programa")
    print ("En caso de no encontrarse este archivo, o de que haya algun error al intentar abrirlo aparecera el siguiente mensaje")
    print ("Ups, hubo un error al intentar abrir el archivo sitedata.json")

    print ("")
    print ("Si al cargar los datos del json, estan en un formato que no corresponda, o de cualquier otro error respecto a esto se mostrara el siguiente mensaje")
    print ("Error, no se pudieron cargar los datos de " + fileName)

    print ("")
    print ("printToken recibe los siguiente argumentos printToken(token, json)")
    print ("La funcion 'printToken' imprime un token especificado, si este no esta imprimira el siguiente mensaje")
    print ("el token " + "'token ingresado por el usuario'" + " no existe")

