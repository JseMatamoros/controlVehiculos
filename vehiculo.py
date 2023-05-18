import csv
class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas
    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas"# los return con ese formato de 3 comilla doble que me pidio
    # def guardar_en_csv(self, archivo):# los 2 metodos recuperar y guardar estan en la clase padre Vehiculo
    #     with open(archivo, mode='a', newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerow([f"<class 'Vehiculo.{type(self).__name__}'>", str(self.__dict__)])
    def guardar_en_csv(self, archivo):
        try:
            with open(archivo, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([f"<class 'Vehiculo.{type(self).__name__}'>", str(self.__dict__)])  
        except (FileNotFoundError, PermissionError):
            print("Error al guardar en el archivo CSV: {e}")
    def leer_en_csv(archivo):
        with open(archivo, mode='r') as file:
            reader = csv.reader(file)
            vehiculos = []
            for row in reader:
                clase = globals()[row[0].split('.')[1][:-2]]
                datos = eval(row[1])
                instancia = clase(**datos)
                vehiculos.append(instancia)
        print("\nImprimiendo instancias por defecto desde el archivo CSV:\n")
        for vehiculo in vehiculos:
            if isinstance(vehiculo, Particular):
                print("Lista de Vehiculos Particular")
            elif isinstance(vehiculo, Carga):
                print("Lista de Vehiculos Carga")
            elif isinstance(vehiculo, Bicicleta):
                print("Lista de Vehiculos Bicicleta")
            elif isinstance(vehiculo, Motocicleta):
                print("Lista de Vehiculos Motocicleta")
            print(vehiculo.__dict__, "\n")
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return f"{super().__str__()}, {self.velocidad} Km/h, {self.cilindrada} cc"
class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_puestos = nro_puestos
    def __str__(self):
        return f"{super().__str__()}, Nro Puestos {self.nro_puestos}"
class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.carga = carga
    def __str__(self):
        return f"{super().__str__()}, Carga: {self.carga} Kg"
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo):
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo = tipo
    def __str__(self):
        return f"{super().__str__()},Tipo: {self.tipo}"
class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios
    def __str__(self):
        return f"{super().__str__()}, Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"