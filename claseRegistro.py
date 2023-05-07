class Registro:
    def __init__(self,temperatura,humedad,presion):
        self.__temperatura=temperatura
        self.__humedad=humedad
        self.__presion=presion

    def __str__(self):
        return f"{self.__temperatura} {self.__humedad} {self.__presion}"
    
    def setTemperatura(self, temperatura):
        self.__temperatura=temperatura

    def setHumedad(self, humedad):
        self.__humedad=humedad

    def setPresionAtmosferica(self,presionAtmosferica):
        self.__presion=presionAtmosferica
    
    def getTemperatura(self):
        return self.__temperatura
    
    def getHumedad(self):
        return self.__humedad
    
    def getPresionAtmosferica(self):
        return self.__presion
    
    

