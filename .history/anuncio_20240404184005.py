# anuncio.py
from error import SubTipoInvalidoError


class Anuncio:
    def __init__(self, ancho, alto, sub_tipo):
        self.__validar_ancho_alto(ancho, alto)
        self.__ancho = ancho
        self.__alto = alto
        self.__validar_sub_tipo(sub_tipo)
        self.__sub_tipo = sub_tipo
        self.__url_archivo = ""
        self.__url_clic = ""

    def __validar_ancho_alto(self, ancho, alto):
        if ancho <= 0:
            self.__ancho = 1
        if alto <= 0:
            self.__alto = 1

    def __validar_sub_tipo(self, sub_tipo):
        sub_tipos_validos = self.SUB_TIPOS
        if sub_tipo not in sub_tipos_validos:
            raise SubTipoInvalidoError(f"Subtipo '{sub_tipo}' inválido para este tipo de anuncio.")

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, valor):
        self.__validar_ancho_alto(valor, self.__alto)
        self.__ancho = valor

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, valor):
        self.__validar_ancho_alto(self.__ancho, valor)
        self.__alto = valor

    @property
    def url_archivo(self):
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, valor):
        self.__url_archivo = valor

    @property
    def url_clic(self):
        return self.__url_clic

    @url_clic.setter
    def url_clic(self, valor):
        self.__url_clic = valor

    @property
    def sub_tipo(self):
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, valor):
        self.__validar_sub_tipo(valor)
        self.__sub_tipo = valor

    @staticmethod
    def mostrar_formatos():
        print("FORMATO 1:")
        print("==========")
        for sub_tipo in Video.SUB_TIPOS:
            print(f"- {sub_tipo}")
        print("\nFORMATO 2:")
        print("==========")
        for sub_tipo in Display.SUB_TIPOS:
            print(f"- {sub_tipo}")
        print("\nFORMATO 3:")
        print("==========")
        for sub_tipo in Social.SUB_TIPOS:
            print(f"- {sub_tipo}")

    def comprimir_anuncio(self):
        pass

    def redimensionar_anuncio(self):
        pass

class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, sub_tipo, duracion):
        super().__init__(1, 1, sub_tipo)
        self.__validar_duracion(duracion)
        self.__duracion = duracion

    def __validar_duracion(self, duracion):
        if duracion <= 0:
            self.__duracion = 5

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, valor):
        self.__validar_duracion(valor)
        self.__duracion = valor

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

class Display(Anuncio):
    FORMATO = "Display" 
    SUB_TIPOS = ("tradicional", "native")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def __init__(self, sub_tipo):
        self.__sub_tipo = sub_tipo
        
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")