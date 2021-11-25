from io import open
Archivo = open('Clasificaciones.txt', 'w')
Tx1 = ('Ingresa las notas de los examenes realizados aqui:')
def Escribir_Datos() :
    Presentacion = 'Bienvenido al Archivo \n'
    Nombre = input ('Ingresa tu nombre aqui : \n')
    Apellido = input ('Ingresa tu apellido aqui : \n')
    Ci = input ('Ingress tu Numero de Cedula de Identidad : \n')
    Semestre = ('Ingrese el semestre que esta cursando: \n')
    Seccion = ('Ingrese en que seccion usted esta cursando: \n')
    print (Tx1)
    n1 = input ('Nota del Primer Examen: \n')
    n2 = input ('Nota del Segundo Examen: \n')
    n3r = input ('Introduzca la tercera nota en caso de haber realizado el examen recuperativo :  \n')
    guardarDatos(Nombre, Apellido , Ci, Semestre, Seccion, n1, n2 , n3r)
    
def guardarDatos(name, last_name , dni, semestre, seccion , n1, n2 , n3r):
    archivo = open('Clasificaciones.txt', 'a')
    archivo.write('\n' + 'Nombre: '+ name)
    archivo.write('\n' + 'Apellido: '+ last_name)
    archivo.write('\n' + 'DNI: '+ dni)
    archivo.write('\n' + 'Semestre: '+ semestre)
    archivo.write('\n' + 'Seccion: '+ seccion)
    archivo.write('\n' + '1era Nota: '+ n1)
    archivo.write('\n' + '2da Nota: '+ n2)
    archivo.write('\n' + 'Recuperativo Nota: '+ n3r)
    archivo.close()
  


def Leer_Datos():
    with open('Clasificaciones.txt', 'r') as f:
        contenido = f.read()
        print(contenido)

def menu():
    print("# MENU ")
    print("1. Agregar Nota")
    print("2. Ver Fichero ")
    print("3. Salir")
    return input(">" )

opcion = 4

while(opcion !=  "3"):
    opcion = menu()
    if opcion == "1": 
        Escribir_Datos()
    elif opcion == "2":
        Leer_Datos()
