from carrera import carrera

class facultad:
    __codigo = ''
    __nombre = ''
    __direccion = ''
    __localidad = ''
    __telefono = ''
    __carrera = list

    def __init__(self,codigo,nombre,dire,loc,tel):
        self.__codigo = int(codigo)
        self.__nombre = nombre
        self.__direccion = dire
        self.__localidad = loc
        self.__telefono = tel
        self.__carrera = []
    
    def cargacarrera(self,cod,nom,fech,dur,tit):
        unacarrera=carrera(cod,nom,fech,dur,tit)
        return self.__carrera.append(unacarrera)
    
    def getcarrera(self):
        return self.__carrera

    def getcodigo(self):
        return self.__codigo
    
    def getnombre(self):
        return self.__nombre
    
    def getdireccion(self):
        return self.__direccion
    
    def getlocalidad(self):
        return self.__localidad
    
    def gettelefono(self):
        return self.__telefono