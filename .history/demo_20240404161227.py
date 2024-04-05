from campaña import Campaña
from error import LargoExcedidoError, SubTipoInvalidoError
from anuncio import Video, Display, Social

# Crear una campaña con un anuncio de video
anuncios = [{"tipo": "Video", "sub_tipo": "instream", "duracion": 30}]
mi_campaña = Campaña("Campaña Inicial", anuncios)

while True:
    try:
        nuevo_nombre = input("Ingrese el nuevo nombre de la campaña: ")
        mi_campaña.nombre = nuevo_nombre

        nuevo_tipo = input("Ingrese el tipo de anuncio (Video, Display, Social): ")
        nuevo_sub_tipo = input("Ingrese el nuevo sub_tipo para el anuncio: ")
        
        if nuevo_tipo == "Video":
            nueva_duracion = int(input("Ingrese la duración del video: "))
            mi_campaña.anuncios[0] = Video(nuevo_sub_tipo, nueva_duracion)  #Video no def
        elif nuevo_tipo == "Display":
            mi_campaña.anuncios[0] = Display(nuevo_sub_tipo)
        elif nuevo_tipo == "Social":
            mi_campaña.anuncios[0] = Social(nuevo_sub_tipo)
        else:
            print("Tipo de anuncio inválido")
            continue

        print(mi_campaña)
        break
    except (LargoExcedidoError, SubTipoInvalidoError, ValueError) as e:
        with open("error.log", "a") as f:
            f.write(str(e) + "\n")
        print("Ocurrió un error:", e)