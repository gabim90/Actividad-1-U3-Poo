from facultad import facultad
import csv

class manejadorfacultad:
    __listafacultad = []
    
    def __init__(self):
        self.__listafacultad = []

    def test(self):
        archivo = open('Facultades.csv')
        reader = csv.reader(archivo,delimiter=',')
        bandera=True
        i=0
        for fila in reader:
           if bandera:
               facu=facultad(fila[0],fila[1],fila[2],fila[3],fila[4])
               self.__listafacultad.append(facu)
               bandera=False
               i=int(fila[0])
           else:    
               if i == int(fila[0]):
                   self.__listafacultad[(len(self.__listafacultad)-1)].cargacarrera(fila[1],fila[2],fila[3],fila[4],fila[5])
               else:    
                   i = int(fila[0])
                   facu=facultad(fila[0],fila[1],fila[2],fila[3],fila[4])
                   self.__listafacultad.append(facu)
    
    def muestrafacultad(self):
        cod=int(input('Ingrese codigo de facultad:'))
        band = True
        i = 0
        while band and i < len(self.__listafacultad):
            if self.__listafacultad[i].getcodigo() == cod:
                band = False
            else:
                i = i + 1
        if band:
            print(" Error no se encontro la facultad")
        else:
            print('Facultad: {}'.format(self.__listafacultad[i].getnombre()))
            for carrera in self.__listafacultad[i].getcarrera():
                print('Carrera: {} Duracion:{}'.format(carrera.getnombrecarrera(), carrera.getduracion()))
    
    def muestracarrera(self):
        nombre=input('Ingrese nombre de carrera:')
        i=0
        b=0
        band=False
        while i<len(self.__listafacultad):
            carreras=self.__listafacultad[i].getcarrera()
            while b<len(carreras):
                if(carreras[b].getnombrecarrera()==nombre):
                    band=True
                else:
                    b=b+1
            if band==True:
                i=len(self.__listafacultad)
            else:
                i=i+1
        if band==True:
            print("Codigo: {}-{} Nombre:{} Localidad:{}".format(self.__listafacultad[i].getcodigo(),carreras[b].getcodigocarrera(),carreras[b].getnombrecarrera(),self.__listafacultad[i].getlocalidad()))
        else:
            print('No se encontro')





        
    
