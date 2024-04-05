from campaña import Campaña
from error import LargoExcedidoError, SubTipoInvalidoError
from anuncio import Video, Display, Social
from anuncio import Anuncio

anuncios = [
    {"tipo": "Video", "sub_tipo": "instream", "duracion": 30},
    {"tipo": "Display", "sub_tipo": "tradicional"},
    {"tipo": "Social", "sub_tipo": "facebook"}
]

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
            mi_campaña.anuncios[0] = Video(nuevo_sub_tipo, nueva_duracion) 
        elif nuevo_tipo == "Display":

            ancho = 300  # Valor de ejemplo para el ancho
            alto = 250   # Valor de ejemplo para el alto
            mi_campaña.anuncios[0] = Display(ancho, alto, nuevo_sub_tipo)
            #mi_campaña.anuncios[0] = Display(nuevo_sub_tipo)
        elif nuevo_tipo == "Social":

            ancho = 300  # Valor de ejemplo para el ancho
            alto = 250   # Valor de ejemplo para el alto
            mi_campaña.anuncios[0] = Social(nuevo_sub_tipo)
            #mi_campaña.anuncios[0] = Social(ancho, alto, nuevo_sub_tipo)
            #mi_campaña.anuncios[0] = Social(nuevo_sub_tipo)
        else:
            print("Tipo de anuncio inválido")
            continue
        
        # Crear instancia de Campaña
        mi_campaña = Campaña("Mi Campaña", anuncios)

        # Llamar al método estático para mostrar los formatos
        Anuncio.mostrar_formatos()
        #print(mi_campaña)
        print(f"Esta campaña: {nuevo_nombre} , será anunciada  mediante un formato {nuevo_tipo}")



        print("*********************Game over******************************")
        break
    except (LargoExcedidoError, SubTipoInvalidoError, ValueError) as e:
        with open("error.log", "a", encoding="utf-8") as f:
            f.write(str(e) + "\n")
        print("Ocurrió un error:", e)