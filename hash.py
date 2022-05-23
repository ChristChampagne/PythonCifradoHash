
import hashlib
import os

def hash_file(filename, algoritmo):

    # Se crea un objeto hash
    h = hashlib.new(algoritmo)
    h.update(str(filename).encode('utf-8'))

    # Abre el archivo para leerlo en modo binario
    with open(filename, 'rb') as file:

        # Lee el contenido del archivo hasta que termina.
        chunk = 0

        # La b significa que esta leyendo el contenido del archivo en bytes.
        while chunk != b'':
            chunk = file.read(1024)

            # Cicla y actualiza el chunk (pedazo del archivo) para leer la información de este. 
            h.update(chunk)

    # Devuelve el resultado en Hexadecimal y con el cifrado asignado.
    return h.hexdigest()


def hash_msg(texto, algoritmo):
    # h = hashlib.md5(str(texto).encode('utf-8'))

    # Se crea un objeto hash y se "Agrega" el algoritmo a la lista, si ya esta, lo utiliza.
    h = hashlib.new(algoritmo)
    
    # Actualiza la biblioteca de hashlib y utiliza el algoritmo anteriormente asignado
    h.update(str(texto).encode('utf-8'))

    # Devuelve el resultado en Hexadecimal
    return h.hexdigest()

salir = 0
while salir == 0:
    error = 1
    
    while error == 1:
        _ = os.system('cls')
        print("""
                                                                 
       _____                               _              _    _           _     
      / ____|                             | |            | |  | |         | |    
     | |  __  ___ _ __   ___ _ __ __ _  __| | ___  _ __  | |__| | __ _ ___| |__  
     | | |_ |/ _ \ '_ \ / _ \ '__/ _` |/ _` |/ _ \| '__| |  __  |/ _` / __| '_ \ 
     | |__| |  __/ | | |  __/ | | (_| | (_| | (_) | |    | |  | | (_| \__ \ | | |
      \_____|\___|_| |_|\___|_|  \__,_|\__,_|\___/|_|    |_|  |_|\__,_|___/_| |_|
                        ---------------------------------
                    by Axel G. Christian E. David A. & Gerardo C.
    
    """)
    
        print("  1.- Cifrar una cadena de texto")
        print("  2.- Cifrar un archivo\n")
    
        opcion = input("  Elige una opción: ")
        if opcion == "1" or opcion == "2":
            error = 0
    
    
    if opcion == "1":
    
        # Limpiar la pantalla para que se vea mejor el resultado
        _ = os.system('cls')
        print("""
                                                                 
       _____                               _              _    _           _     
      / ____|                             | |            | |  | |         | |    
     | |  __  ___ _ __   ___ _ __ __ _  __| | ___  _ __  | |__| | __ _ ___| |__  
     | | |_ |/ _ \ '_ \ / _ \ '__/ _` |/ _` |/ _ \| '__| |  __  |/ _` / __| '_ \ 
     | |__| |  __/ | | |  __/ | | (_| | (_| | (_) | |    | |  | | (_| \__ \ | | |
      \_____|\___|_| |_|\___|_|  \__,_|\__,_|\___/|_|    |_|  |_|\__,_|___/_| |_|
                        ---------------------------------
                    by Axel G. Christian E. David A. & Gerardo C.
    
    """)
        text_cifrar = str(input("\n\n  Ingresa el mensaje a cifrar: "))
    
        # Se asignan todos los algoritmos a la variable algoritmos mediante la libreria hashlib.
        algortimos = set(hashlib.algorithms_available)
    
        # Se crea un array para segregar los cifrados shake y estos no aparezcan en la lista de cifrados
        no_mostrar = set(['shake_128', 'shake_256'])
        
        # Mediante el uso de set se segregan los algoritmos.
        algoritmos_disponibles = algortimos - no_mostrar
    
        # Se imprimen los algoritmos ya segregados.
        error = 1
        while error == 1:
            # Limpiar la pantalla para que se vea mejor el resultado
            _ = os.system('cls')
            print("""
       _____                               _              _    _           _     
      / ____|                             | |            | |  | |         | |    
     | |  __  ___ _ __   ___ _ __ __ _  __| | ___  _ __  | |__| | __ _ ___| |__  
     | | |_ |/ _ \ '_ \ / _ \ '__/ _` |/ _` |/ _ \| '__| |  __  |/ _` / __| '_ \ 
     | |__| |  __/ | | |  __/ | | (_| | (_| | (_) | |    | |  | | (_| \__ \ | | |
      \_____|\___|_| |_|\___|_|  \__,_|\__,_|\___/|_|    |_|  |_|\__,_|___/_| |_|
                        ---------------------------------
                    by Axel G. Christian E. David A. & Gerardo C.
    
    """)
            print("\n\n  Algoritmos de cifrado disponibles: \n\n{}".format(
                ', '.join(sorted(algoritmos_disponibles))))
            alg_seleccionado = str(input(
                "\n  Ingresa el nombre del algoritmo que deseas utilizar para cifrar tu mensaje: "))
    
            # Validar que el algoritmo de cifrado elegido por el usuario esté en la lista disponible
            for cifrado in algoritmos_disponibles:
                if alg_seleccionado == cifrado:
                    error = 0
                    msg_cifrado = hash_msg(text_cifrar, alg_seleccionado)
    if opcion == "2":
        # Limpiar la pantalla para que se vea mejor el resultado
        _ = os.system('cls')
        print("""
       _____                               _              _    _           _     
      / ____|                             | |            | |  | |         | |    
     | |  __  ___ _ __   ___ _ __ __ _  __| | ___  _ __  | |__| | __ _ ___| |__  
     | | |_ |/ _ \ '_ \ / _ \ '__/ _` |/ _` |/ _ \| '__| |  __  |/ _` / __| '_ \ 
     | |__| |  __/ | | |  __/ | | (_| | (_| | (_) | |    | |  | | (_| \__ \ | | |
      \_____|\___|_| |_|\___|_|  \__,_|\__,_|\___/|_|    |_|  |_|\__,_|___/_| |_|
                        ---------------------------------
                    by Axel G. Christian E. David A. & Gerardo C.
    
         """)
        nom_archivo = str(
            input("""\n\n  Ingresa el nombre del archivo con extensión que quieres cifrar 
            (El archivo debe de estar en el mismo directorio que el generador hash): """))
    
        # Limpiar la pantalla para que se vea mejor el resultado
        _ = os.system('cls')
    
        # Se asignan todos los algoritmos a la variable algoritmos mediante la libreria hashlib.
        algortimos = set(hashlib.algorithms_available)
    
        # Se crea un array para segregar los cifrados shake y estos no aparezcan en la lista de cifrados
        no_mostrar = set(['shake_128', 'shake_256'])
    
        # Mediante el uso de set se segregan los algoritmos.
        algoritmos_disponibles = algortimos - no_mostrar
    
        error = 1
        while error == 1:
            # Limpiar la pantalla para que se vea mejor el resultado
            _ = os.system('cls')
            print("""
       _____                               _              _    _           _     
      / ____|                             | |            | |  | |         | |    
     | |  __  ___ _ __   ___ _ __ __ _  __| | ___  _ __  | |__| | __ _ ___| |__  
     | | |_ |/ _ \ '_ \ / _ \ '__/ _` |/ _` |/ _ \| '__| |  __  |/ _` / __| '_ \ 
     | |__| |  __/ | | |  __/ | | (_| | (_| | (_) | |    | |  | | (_| \__ \ | | |
      \_____|\___|_| |_|\___|_|  \__,_|\__,_|\___/|_|    |_|  |_|\__,_|___/_| |_|
                        ---------------------------------
                    by Axel G. Christian E. David A. & Gerardo C.
    
        """)
            print("\n\n  Cifrados disponibles:\n{}".format(
                ', '.join(sorted(algoritmos_disponibles))))
            alg_seleccionado = str(input(
                "\n\n  Ingresa el nombre del algoritmo que deseas utilizar para cifrar tu archivo: "))
    
            # Validar que el algoritmo de cifrado elegido por el usuario esté en la lista disponible
            for cifrado in algoritmos_disponibles:
                if alg_seleccionado == cifrado:
                    error = 0
                    msg_cifrado = hash_file(nom_archivo, alg_seleccionado)     

    # Limpiar la pantalla para que se vea mejor el resultado
    _ = os.system('cls')
    print("""
       _____                               _              _    _           _     
      / ____|                             | |            | |  | |         | |    
     | |  __  ___ _ __   ___ _ __ __ _  __| | ___  _ __  | |__| | __ _ ___| |__  
     | | |_ |/ _ \ '_ \ / _ \ '__/ _` |/ _` |/ _ \| '__| |  __  |/ _` / __| '_ \ 
     | |__| |  __/ | | |  __/ | | (_| | (_| | (_) | |    | |  | | (_| \__ \ | | |
      \_____|\___|_| |_|\___|_|  \__,_|\__,_|\___/|_|    |_|  |_|\__,_|___/_| |_|
                        ---------------------------------
                    by Axel G. Christian E. David A. & Gerardo C.
    
    """)
    print("\n\n  Hash " + alg_seleccionado + ": " + msg_cifrado)
    salir = int(input("\n\n  Presiona la tecla 0 para volver al menú o cualquier otra tecla para salir: "))
