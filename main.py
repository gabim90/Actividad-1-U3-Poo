from manejadorfacultad import manejadorfacultad

if __name__=='__main__':
    lista=manejadorfacultad()
    lista.test()
    opc=int(input('Ingrese codigo:'))
    print('1-Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.')
    print('2-Ingresar nombre de carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.')
    while opc!=0:
        if(opc==1):
            lista.muestrafacultad()
        elif(opc==2):
            lista.muestracarrera()
        opc=int(input('Ingrese codigo, finalize con:'))