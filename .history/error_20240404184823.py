# error.py

class Error(Exception):
    pass

class LargoExcedidoError(Error):
    def __init__(self, mensaje):
        self.mensaje = mensaje

class SubTipoInvalidoError(Error):
    def __init__(self, mensaje):
        self.mensaje = mensaje
