# campaña.py
from anuncio import Video, Display, Social
from error import LargoExcedidoError

class Campaña:
    def __init__(self, nombre, anuncios):
        self.__validar_nombre(nombre)
        self.__nombre = nombre
        self.__fecha_inicio = None
        self.__fecha_termino = None
        self.__anuncios = self.__crear_anuncios(anuncios)

    def __validar_nombre(self, nombre):
        if len(nombre) > 250:
            raise LargoExcedidoError("El nombre de la campaña excede los 250 caracteres.")

    def __crear_anuncios(self, anuncios_data):
        anuncios = []
        for anuncio_data in anuncios_data:
            tipo = anuncio_data["tipo"]
            sub_tipo = anuncio_data["sub_tipo"]
            if tipo == "Video":
                duracion = anuncio_data["duracion"]
                anuncio = Video(sub_tipo, duracion)
            elif tipo == "Display":
                anuncio = Display(sub_tipo)
            elif tipo == "Social":
                anuncio = Social(sub_tipo)
            anuncios.append(anuncio)
        return anuncios

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__validar_nombre(valor)
        self.__nombre = valor

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, valor):
        self.__fecha_inicio = valor

    @property
    def fecha_termino(self):
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, valor):
        self.__fecha_termino = valor

    @property
    def anuncios(self):
        return self.__anuncios

    def __str__(self):
        conteo_anuncios = {
            "Video": 0,
            "Display": 0,
            "Social": 0
        }
        for anuncio in self.__anuncios:
            tipo = type(anuncio).__name__
            conteo_anuncios[tipo] += 1

        resultado = f"Nombre de la campaña: {self.__nombre}\n"
        resultado += "Anuncios: "
        resultado += ", ".join(f"{cantidad