#Jugar en la nueva consola que incluye windows o en una consola que reproduzca emojis y colores, si se usa el CMD de toda la vida va a dar errores graficos por todos lados.

#La nueva consola de windows se llama wt.exe.

import random

FILAS = 0
COLUMNAS = 0
MINAS = 0
banderaCorrectas = 0
minasTotales = ""
tablero = ""
tableroMostrado = ""
final = False

asciiArtPython = r"""
   _ (`-.               .-') _    ('-. .-.                  .-') _                                                                 
  ( (OO  )             (  OO) )  ( OO )  /                 ( OO ) )                                                                
 _.`     \  ,--.   ,--./     '._ ,--. ,--. .-'),-----. ,--./ ,--,'                                                                 
(__...--''   \  `.'  / |'--...__)|  | |  |( OO'  .-.  '|   \ |  |\                                                                 
 |  /  | | .-')     /  '--.  .--'|   .|  |/   |  | |  ||    \|  | )                                                                
 |  |_.' |(OO  \   /      |  |   |       |\_) |  |\|  ||  .     |/                                                                 
 |  .___.' |   /  /\_     |  |   |  .-.  |  \ |  | |  ||  |\    |                                                                  
 |  |      `-./  /.__)    |  |   |  | |  |   `'  '-'  '|  | \   |                                                                  
 `--'        `--'         `--'   `--' `--'     `-----' `--'  `--'
"""
asciiArtBM = r"""
.-. .-')                 .-')                ('-.           _   .-')                 .-') _    ('-.      .-')                      
\  ( OO )               ( OO ).             ( OO ).-.      ( '.( OO )_              ( OO ) )  ( OO ).-. ( OO ).                    
 ;-----.\  ,--. ,--.   (_)---\_)   .-----.  / . --. /       ,--.   ,--.) ,-.-') ,--./ ,--,'   / . --. /(_)---\_)                   
 | .-.  |  |  | |  |   /    _ |   '  .--./  | \-.  \        |   `.'   |  |  |OO)|   \ |  |\   | \-.  \ /    _ |                    
 | '-' /_) |  | | .-') \  :` `.   |  |('-..-'-'  |  |       |         |  |  |  \|    \|  | ).-'-'  |  |\  :` `.                    
 | .-. `.  |  |_|( OO ) '..`''.) /_) |OO  )\| |_.'  |       |  |'.'|  |  |  |(_/|  .     |/  \| |_.'  | '..`''.)                   
 | |  \  | |  | | `-' /.-._)   \ ||  |`-'|  |  .-.  |       |  |   |  | ,|  |_.'|  |\    |    |  .-.  |.-._)   \                   
 | '--'  /('  '-'(_.-' \       /(_'  '--'\  |  | |  |       |  |   |  |(_|  |   |  | \   |    |  | |  |\       /                   
 `------'   `-----'     `-----'    `-----'  `--' `--'       `--'   `--'  `--'   `--'  `--'    `--' `--' `-----' 
"""
asciiArtPB = r"""
   _ (`-.              _  .-')        .-. .-')    ('-.   .-') _      ('-.                                                          
  ( (OO  )            ( \( -O )       \  ( OO ) _(  OO) (  OO) )    ( OO ).-.                                                      
 _.`     \ .-'),-----. ,------.        ;-----.\(,------./     '._   / . --. /                                                      
(__...--''( OO'  .-.  '|   /`. '       | .-.  | |  .---'|'--...__)  | \-.  \                                                       
 |  /  | |/   |  | |  ||  /  | |       | '-' /_)|  |    '--.  .--'.-'-'  |  |                                                      
 |  |_.' |\_) |  |\|  ||  |_.' |       | .-. `.(|  '--.    |  |    \| |_.'  |                                                      
 |  .___.'  \ |  | |  ||  .  '.'       | |  \  ||  .--'    |  |     |  .-.  |                                                      
 |  |        `'  '-'  '|  |\  \        | '--'  /|  `---.   |  |     |  | |  |                                                      
 `--'          `-----' `--' '--'       `------' `------'   `--'     `--' `--'     
"""
asciiArtPL = r"""
   _ (`-.    ('-.     _  .-')     ('-.                                _   .-')       ('-.   .-') _   _  .-')                       
  ( (OO  )  ( OO ).-.( \( -O )   ( OO ).-.                           ( '.( OO )_   _(  OO) (  OO) ) ( \( -O )                      
 _.`     \  / . --. / ,------.   / . --. /       ,--.     ,--. ,--.   ,--.   ,--.)(,------./     '._ ,------.  ,-.-')  .-'),-----. 
(__...--''  | \-.  \  |   /`. '  | \-.  \        |  |.-') |  | |  |   |   `.'   |  |  .---'|'--...__)|   /`. ' |  |OO)( OO'  .-.  '
 |  /  | |.-'-'  |  | |  /  | |.-'-'  |  |       |  | OO )|  | | .-') |         |  |  |    '--.  .--'|  /  | | |  |  \/   |  | |  |
 |  |_.' | \| |_.'  | |  |_.' | \| |_.'  |       |  |`-' ||  |_|( OO )|  |'.'|  | (|  '--.    |  |   |  |_.' | |  |(_/\_) |  |\|  |
 |  .___.'  |  .-.  | |  .  '.'  |  .-.  |      (|  '---.'|  | | `-' /|  |   |  |  |  .--'    |  |   |  .  '.',|  |_.'  \ |  | |  |
 |  |       |  | |  | |  |\  \   |  | |  |       |      |('  '-'(_.-' |  |   |  |  |  `---.   |  |   |  |\  \(_|  |      `'  '-'  '
 `--'       `--' `--' `--' '--'  `--' `--'       `------'  `-----'    `--'   `--'  `------'   `--'   `--' '--' `--'        `-----' 
"""
                                                    
print("\033[32m" + asciiArtPython, end="")
print("\033[33m" + asciiArtBM, end="")
print("\033[34m" + asciiArtPB, end="")
print("\033[31m" + asciiArtPL, end="" + "\033[0m")

def dificultad():
    global MINAS
    print("Elegir dificultad: ")
    print(" 1- Principiante")
    print(" 2- Intermedio")
    print(" 3- Experto")
    print(" 4- Personalizado")
    while True:
        try:
            eleccion = int(input("(Elige un numero acorde a la dificultad deseada, ejemplo: Principante es 1 ): "))
            if eleccion in [1, 2, 3, 4]:
                if eleccion == 1:
                    FILAS = 8
                    COLUMNAS = 8
                    MINAS = 10
                elif eleccion == 2:
                    FILAS = 16
                    COLUMNAS = 16
                    MINAS = 40
                elif eleccion == 3:
                    FILAS = 16
                    COLUMNAS = 31
                    MINAS = 99
                elif eleccion == 4:        
                    FILAS = int(input("Numero de filas: (El minimo es 1, el maximo es 32 debido a limitaciónes de python.) "))
                    COLUMNAS = int(input("Numero de columnas: (El minimo es 1, el maximo es 32 debido a limitaciónes de python.) "))
                    MINAS = int(input("Numero de bombas: (El maximo es las Filas * las Columnas, ejemplo tablero 9*9 = 81 (Maximo de 81 minas.)) "))

                while FILAS > 32 or FILAS <= 0 or COLUMNAS > 32 or COLUMNAS <= 0 or MINAS > FILAS * COLUMNAS:
                    print("Creo haberte dicho que el maximo era 32 y que no usaras 0 por motivos obvios tampoco deberías poner más minas de las casillas que tiene el tablero 🤨")
                    FILAS = int(input("Numero de filas: (El maximo es 32 debido a limitaciónes de python.) "))
                    COLUMNAS = int(input("Numero de columnas: (El maximo es 32 debido a limitaciónes de python.) "))
                    MINAS = int(input("Numero de bombas: (El maximo es las Filas * las Columnas, ejemplo tablero 9*9 = 81 (Maximo de 81 minas.)) "))

                return FILAS, COLUMNAS, MINAS
        except ValueError:
            print("Porfavor elige una opción valida.")


FILAS, COLUMNAS, MINAS = dificultad()

tablero = [["." for _ in range(COLUMNAS)] for _ in range(FILAS)]

tableroMostrado = [["🔲" for _ in range(COLUMNAS)] for _ in range(FILAS)]

minas = random.sample([(i, j) for i in range(FILAS) for j in range(COLUMNAS)], MINAS)
for minar in minas:
    tablero[minar[0]][minar[1]] = "💣"

def contarMinas(fila, columna):
    contador = 0
    for i in range(fila-1, fila+2):
        for j in range(columna-1, columna+2):
            if 0 <= i < FILAS and 0 <= j < COLUMNAS and (i, j) != (fila, columna) and tablero[i][j] == "💣":
                contador += 1
    return contador

def revelar(fila, columna):
    if tablero[fila][columna] != "0":
        if tablero[fila][columna] == "1":
            tableroMostrado[fila][columna] = "\033[1;31m" + tablero[fila][columna] + "\033[0m" + " "
        elif tablero[fila][columna] == "2":
            tableroMostrado[fila][columna] = "\033[1;32m" + tablero[fila][columna] + "\033[0m" + " "
        elif tablero[fila][columna] == "3":
            tableroMostrado[fila][columna] = "\033[1;33m" + tablero[fila][columna] + "\033[0m" + " "
        elif tablero[fila][columna] == "4":
            tableroMostrado[fila][columna] = "\033[1;34m" + tablero[fila][columna] + "\033[0m" + " "
        elif tablero[fila][columna] == "5":
            tableroMostrado[fila][columna] = "\033[1;35m" + tablero[fila][columna] + "\033[0m" + " "
        elif tablero[fila][columna] == "6":
            tableroMostrado[fila][columna] = "\033[1;36m" + tablero[fila][columna] + "\033[0m" + " "
        elif tablero[fila][columna] == "7":
            tableroMostrado[fila][columna] = "\033[92m" + tablero[fila][columna] + "\033[0m" + " "
        elif tablero[fila][columna] == "8":
            tableroMostrado[fila][columna] = "\033[94m" + tablero[fila][columna] + "\033[0m" + " "
        return
    tableroMostrado[fila][columna] = tablero[fila][columna] + " "
    for i in range(fila-1, fila+2):
        for j in range(columna-1, columna+2):
            if 0 <= i < FILAS and 0 <= j < COLUMNAS and tableroMostrado[i][j] == "🔲":
                revelar(i, j)

def ponerBandera(fila, columna):
    if tableroMostrado[fila][columna] == "🚩":
        tableroMostrado[fila][columna] = "🔲"
        return False
    elif tableroMostrado[fila][columna] == "🔲":
        tableroMostrado[fila][columna] = "🚩"
        return True
    else:
        return False

def resetearElJuego():
    global tablero, tableroMostrado, minasTotales, banderaCorrectas
    tablero = ""
    tableroMostrado = ""
    banderaCorrectas = 0
    FILAS, COLUMNAS, MINAS = dificultad()
    minasTotales = MINAS
    tablero = [["." for _ in range(COLUMNAS)] for _ in range(FILAS)]
    tableroMostrado = [["🔲" for _ in range(COLUMNAS)] for _ in range(FILAS)]
    minas = random.sample([(i, j) for i in range(FILAS) for j in range(COLUMNAS)], MINAS)
    for minar in minas:
        tablero[minar[0]][minar[1]] = "💣"
    banderaCorrectas = 0
        
def juego():
    global FILAS, COLUMNAS, MINAS, banderaCorrectas, minasTotales, tablero, tableroMostrado, final
    FILAS, COLUMNAS, MINAS = dificultad()
    tablero = [["." for _ in range(COLUMNAS)] for _ in range(FILAS)]
    tableroMostrado = [["🔲" for _ in range(COLUMNAS)] for _ in range(FILAS)]
    minas = random.sample([(i, j) for i in range(FILAS) for j in range(COLUMNAS)], MINAS)
    for minar in minas:
        tablero[minar[0]][minar[1]] = "💣"
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if tablero[i][j] != "💣":
                tablero[i][j] = str(contarMinas(i, j))
    banderaCorrectas = 0
    minasTotales = MINAS
    final = False

for i in range(FILAS):
    for j in range(COLUMNAS):
        if tablero[i][j] != "💣":
            tablero[i][j] = str(contarMinas(i, j)) 
while not final:

    if banderaCorrectas == minasTotales and banderaCorrectas < minasTotales:
        print("Ganaste!")
        final = True
        resetearElJuego()

    for fila in tableroMostrado:
        print(" ".join(fila))

    eleccionUsuario = input("Elige una acción (B/bandera para poner una bandera, o las coordenadas que deseas revelar (x y)): ")
    if eleccionUsuario.lower() in ["b", "bandera"]:
        eleccionUsuario = input("Elige la fila y la columna para poner la bandera: ")
        try:
            fila, columna = map(int, eleccionUsuario.split())
        except ValueError:
            print("Parece que el valor que elegiste no es valido, recuerda que debe ser así: x y donde 'x' es la fila y 'y' la columna.")
            continue
        if ponerBandera(fila, columna):
            if tablero[fila][columna] == "💣":
                banderaCorrectas += 1
        else:
            print("Este sitio ya habia sido revelado, o tiene una bandera encima.")
    else:
        try:
            fila, columna = map(int, eleccionUsuario.split())
        except ValueError:
            print("Parece que el valor que elegiste no es valido, recuerda que debe ser así: x y donde 'x' es la fila y 'x' la columna.")
            continue
        
    if 0 <= fila < FILAS and 0 <= columna < COLUMNAS:
            if tableroMostrado[fila][columna] != "🔲":
                print("Este sitio ya habia sido revelado, o tiene una bandera encima.")
                continue
            if tablero[fila][columna] == "💣":
                print("Se acabó el juego!")
                for i in range(FILAS):
                    for j in range(COLUMNAS):
                        if tablero[i][j] == "💣":
                            tableroMostrado[i][j] = "💣"
                for fila in tableroMostrado:
                    print(" ".join(fila))
                print("Perdiste!")
                final = True
            if final:
                repetirJuego = input("¿Quieres jugar de nuevo? (S/N): ")
                while repetirJuego.lower() != "s" and repetirJuego.lower() != "n":
                    repetirJuego = input("Introduce una opción valida: ")
                if repetirJuego.lower() == "s":
                    juego()
                elif repetirJuego.lower() == "n":
                    break
            else:
                tableroMostrado[fila][columna] = tablero[fila][columna] + " "
                revelar(fila, columna)
    else:
            print("Porfavor introduce coordenadas acordes al tablero: ")
