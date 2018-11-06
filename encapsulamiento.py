
class Engine(object):
    #Constructor
    def __init__(self, type, hp, brand):
        self.__type = type #Diesel, Gas, Electric
        self.__hp = hp #Horse Power
        self.__brand = brand #Marca
        self.__is_on = False #Encendido
        self.__rpm = 0 #Revoluciones por minuto

    @property #Decorador (muestra el metodo como una propiedad
    def is_on(self):
        #Solo retorna el valor pero no permite
        # que alguien mas modifique el estado
        return self.__is_on
    #Metodo para encender el motor si esta apagado
    def turn_on(self):
        if not self.is_on:
            self.__is_on = True
    #Metodo para apagar el motor si esta encendido
    def  turn_off(self):
        if self.__is_on:
            self.__is_on = False

#--------------------------------------------------------------
#CLASS VEHICLE
#--------------------------------------------------------------
class Vehiculo(object):

    def __init__(self, engine=None, color="grey", make="Tata",
        transmission = "manual"):
        self.__init_engine(engine)
        self.__color = None
        self.__make = None
        self.__transmission = None

    def __init_engine(self, engine):
        if engine:
            self.__engine = engine
        else:
            self.__engine = Engine("diesel", 80, "tata")

    def is_on(self):
        return self.__engine.is_on

    def turn_on(self):
        self.__engine.turn_on()

    def turn_off(self):
        self.__engine.turn_off()

    def switch_engine(self, engine):
        self.__engine = engine


class Tank(Vehiculo):

    def __init__(self, engine=None, color="grey", make="Tata",
        transmission = "manual", caliber=35):
        # Primero llamamos a la logica de inicializacion del padre
        # super == padre
        super().__init__(engine, color, make,  transmission)
        self.caliber = caliber

    def shoot():
        return True


car = Tank(engine=None, color="red", make="audi", caliber=90)

if not car.is_on:
    print("El carro esta apagado")

car.switch_engine(Engine("electric",250, "Tesla")

#car.turn_on()

#if car.is_on:
#    print("El carro esta encendido")