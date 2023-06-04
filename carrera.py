
class carrera:
    __codigoc = ''
    __nombrec = ''
    __especialidad = ''
    __duracion = ''
    __titulo = ''

    def __init__(self,cod,nomb,esp,dur,tit):
        self.__codigoc = int(cod)
        self.__nombrec = nomb
        self.__especialidad= esp
        self.__duracion = dur
        self.__titulo = tit
    
    def getespecialidad(self):
        return self.__especialidad

    def getcodigocarrera(self):
        return self.__codigoc
    
    def getnombrecarrera(self):
        return self.__nombrec
    
    def getduracion(self):
        return self.__duracion
    
    def gettitulo(self):
        return self.__titulo