def minmaxtemp(registro):
    tempmin=registro[0][0].getTemperatura()
    tempmax=registro[0][0].getTemperatura()
    diamin=0
    horamin=0
    diamax=0
    horamax=0
    for i in range(31):
        for j in range(24):
            if registro[i][j].getTemperatura()<tempmin:
                tempmin=registro[i][j].getTemperatura()
                diamin=i
                horamin=j
            if registro[i][j].getTemperatura()>tempmax:
                tempmax=registro[i][j].getTemperatura()
                diamax=i
                horamax=j
    print(f"La temperatura minima fue en el dia: {diamin+1} a las {horamin} hrs y fue de: {tempmin} grados")
    print(f"La temperatura máxima fue en el dia: {diamax+1} a las {horamax} hrs y fue de: {tempmax} grados")

def minmaxhum(registro):
    hummin=registro[0][0].getHumedad()
    hummax=registro[0][0].getHumedad()
    diamin=0
    horamin=0
    diamax=0
    horamax=0
    for i in range(31):
        for j in range(24):
            if registro[i][j].getHumedad()<hummin:
                hummin=registro[i][j].getHumedad()
                diamin=i
                horamin=j
            if registro[i][j].getHumedad()>hummax:
                hummax=registro[i][j].getHumedad()
                diamax=i
                horamax=j
    print(f"La humedad minima fue en el dia: {diamin+1} a las {horamin} hrs y fue de: {hummin}")
    print(f"La humedad máxima fue en el dia: {diamax+1} a las {horamax} hrs y fue de: {hummax}")

def minmaxpres(registro):
    presmin=registro[0][0].getPresionAtmosferica()
    presmax=registro[0][0].getPresionAtmosferica()
    diamin=0
    horamin=0
    diamax=0
    horamax=0
    for i in range(31):
        for j in range(24):
            if registro[i][j].getPresionAtmosferica()<presmin:
                presmin=registro[i][j].getPresionAtmosferica()
                diamin=i
                horamin=j
            if registro[i][j].getPresionAtmosferica()>presmax:
                presmax=registro[i][j].getPresionAtmosferica()
                diamax=i
                horamax=j
    print(f"La presion atmosferica minima fue en el dia: {diamin+1} a las {horamin} hrs y fue de: {presmin}")
    print(f"La presion atmosferica máxima fue en el dia: {diamax+1} a las {horamax} hrs y fue de: {presmax}")