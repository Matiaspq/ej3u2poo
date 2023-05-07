import csv
from claseRegistro import Registro
from minmax import minmaxtemp, minmaxhum, minmaxpres

if __name__ == '__main__':
    registroMensual=[]
    for i in range(31):
        registroDia=[]
        for j in range(24):
            registro=Registro(0,0,0)
            registroDia.append(registro)
        registroMensual.append(registroDia)

    archivo = open('archivo.csv')
    reader = csv.reader(archivo, delimiter=',')
    next(reader)
    print("\n----------------Archivo---------------")
    for fila in reader:
        dia=int(fila[0])
        hora=int(fila[1])
        registroMensual[dia-1][hora].setTemperatura(float(fila[2]))
        registroMensual[dia-1][hora].setHumedad(float(fila[3]))
        registroMensual[dia-1][hora].setPresionAtmosferica(float(fila[4]))
    minmaxtemp(registroMensual)
    minmaxhum(registroMensual)
    minmaxpres(registroMensual)

    


    temperaturaPromedio = [0] * 24
    print(temperaturaPromedio)

