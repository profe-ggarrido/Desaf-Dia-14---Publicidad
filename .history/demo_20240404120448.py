from campaña import Campaña
from error import LargoExcedidoError, SubTipoInvalidoError

# Crear una campaña con un anuncio de video
anuncios = [{"tipo": "Video", "sub_tipo": "instream", "duracion": 30}]
mi_campaña = Campaña("Campaña Inicial", anuncios)

while True:
    try:
        nuevo_nombre = input("Ingrese el nuevo nombre de la campaña: ")
        mi_campaña.nombre = nuevo_nombre
        
        nuevo_sub_tipo = input("Ingrese el nuevo sub_tipo para el anuncio: ")
        mi_campaña.anuncios[0].sub_tipo = nuevo_sub_tipo
        
        print(mi_campaña)
        break
    except (LargoExcedidoError, SubTipoInvalidoError) as e:
        with open("error.log", "a") as f:
            f.write(str(e) + "\n")
        print("Ocurrió un error:", e)