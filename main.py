from vehiculo import *
import os
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    limpiar_pantalla()
    while True:
        try: #try except para ValueError de n
            n = int(input("Cuantos Vehiculos desea insertar: ")) # el campo no puede estar vacio
            if n > 0:
                break
            else:
                input("Error: El numero de vehículos debe ser mayor que 0, PRESIONE ENTER!")
        except ValueError:
            input("Error: Ingrese un numero entero valido para el numero de vehiculos, PRESIONE ENTER!")
    vehiculos = []
    for i in range(n):
        limpiar_pantalla()
        print(f"Datos del automovil {i+1}")
        while True:
            marca = input("Inserte la marca del automovil: ")
            if marca.strip():
                break
            else:
                input("Error: ¡La marca no puede estar vacia!, PRESIONE ENTER!")
        while True:
            modelo = input("Inserte el modelo: ")
            if modelo.strip():
                break
            else:
                input("Error: ¡El modelo no puede estar vacio!, PRESIONE ENTER!")
        while True:
            try:
                nro_ruedas = int(input("Inserte el numero de ruedas: "))
                break
            except ValueError:
                input("Error: ¡Ingrese un numero valido para el numero de ruedas!, PRESIONE ENTER!")
        while True:
            velocidad = input("Inserte la velocidad en km/h: ")
            if velocidad.strip():
                break
            else:
                input("Error: ¡La velocidad no puede estar vacia!, PRESIONE ENTER!")
        while True:
            cilindrada = input("Inserte el cilindraje en cc: ")
            if cilindrada.strip():
                break
            else:
                input("Error: ¡El cilindraje no puede estar vacio, PRESIONE ENTER!")
        while True:
            try:
                vehiculo = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
                vehiculos.append(vehiculo)
                break
            except Exception as error:
                input(f"Error al ingresar los datos del automovil {i+1}: {str(error)}, PRESIONE ENTER!")
                input(f"Vuelva a ingresar el dato incorrecto: {error}, PRESIONE ENTER!")
    limpiar_pantalla() 
    print("Imprimiendo por pantalla los Vehiculos:\n")
    for i, vehiculo in enumerate(vehiculos): # recorremos la lista "vehiculos" e imprimimos cada "vehiculo"
        print(f"Datos del automovil {i+1} :{vehiculo}") # imprimimos cada vehiculo con su indice y su contenido con esactamente el mismo formato solicitado en la evaluacion
    particular = Particular("Ford", "Fiesta", 4, "180", "500", 5) # instancias pedidas en el ejercicio
    carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)
    print("\nImprimiento instancias por defecto directo en pantalla\n")
    print(f"{particular}")
    print(f"{carga}")
    print(f"{bicicleta}")
    print(f"{motocicleta}")
    print("\nVerificacion de relaciones entre instancias y clase:\n")# las verificaciones tal cual  las solicitan en el ejercicio
    print(f"Motocicleta es instancia con relacion a Vehiculo: {isinstance(motocicleta, Vehiculo)}")
    print(f"Motocicleta es instancia con relacion a Automovil: {isinstance(motocicleta, Automovil)}")
    print(f"Motocicleta es instancia con relacion a Vehiculo particular: {isinstance(motocicleta, Particular)}")
    print(f"Motocicleta es instancia con relacion a Vehiculo de Carga: {isinstance(motocicleta, Carga)}")
    print(f"Motocicleta es instancia con relacion a Bicicleta: {isinstance(motocicleta, Bicicleta)}")
    print(f"Motocicleta es instancia con relacion a Motocicleta: {isinstance(motocicleta, Motocicleta)}")
    particular.guardar_en_csv('vehiculo.csv')# usamos el metodo creado que proviene de Vehiculo
    carga.guardar_en_csv('vehiculo.csv')# asi guardamos las instancias tal cual solicitan en el ejercicio
    bicicleta.guardar_en_csv('vehiculo.csv')
    motocicleta.guardar_en_csv('vehiculo.csv')
    Vehiculo.leer_en_csv('vehiculo.csv')# la lectura con el metodo para recuperar desdeel archivo csv se aplicadesde Vehiculo
if __name__ == '__main__':# esto decidi agregarlo por que lei que era una buena practica 
    main() # llamamos a la funcion main cuando el archivo se ejecuta directamente como un programa, y no cuando se importa como un modulo en otro archivo