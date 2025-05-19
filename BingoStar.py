import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os


def borrar_archivos(lista_path):
    for elemento in lista_path:
        if os.path.exists(elemento):
            os.remove(elemento)

def confirmar_borrado():
    respuesta = messagebox.askyesno("Confirmar Borrado", "¿Estás seguro de que quieres borrar los archivos?")
    if respuesta:
        confirmar_borrado_final()

def confirmar_borrado_final():
    respuesta_final = messagebox.askyesno("Confirmar Borrado Final", "Acepto la advertencia de borrar y quiero continuar.")
    if respuesta_final:
        borrar_archivos(lista_path)


def actualizar_longitud_numeros():
    label_longitud_numeros.config(text=f"Longitud de números cantados: {len(numerosCantados)}")
    menu.after(1, actualizar_longitud_numeros)
def guardar_en_csv(codigos_info, archivo_csv):
    # Verificamos si el archivo CSV ya existe
    existe_archivo = os.path.exists(archivo_csv)

    # Abrimos el archivo en modo de escritura, usando newline='' para manejar correctamente los saltos de línea
    with open(archivo_csv, 'a', newline='', encoding='utf-8') as csvfile:
        # Definimos el escritor CSV
        fieldnames = ['Codigo', 'Info']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Escribimos cada entrada de codigos_info en el CSV
        for codigo, info in codigos_info:
            writer.writerow({'Codigo': codigo, 'Info': info})


def revertir_ultimo_numero():
    if numerosCantados:
        ultimo_numero = numerosCantados.pop()
        # Habilitar el botón correspondiente
        botones_numeros[ultimo_numero - 1].config(state=tk.NORMAL)
        verificar()
        with open(rutaCSVDeTablasGanadoras, 'w', newline='') as archivo:
            archivo.write('')

def string_a_lista_numeros(cadena):
    numeros_str = cadena.split(',')
    numeros = [int(numero) for numero in numeros_str]
    return numeros

def agregar_numero(numero):
    if numero not in numerosCantados:
        numerosCantados.append(numero)
        # Deshabilitar el botón correspondiente
        botones_numeros[numero - 1].config(state=tk.DISABLED)
        verificar()
def verificar():
    global ventana_resultados
    codigosGanadores = set()
    codigosGanadoresInfo = []
    # Verificar filas, columnas y esquinas simultáneamente
    for tabla in filas:
        codigo = tabla[0]
        conjunto_filas = tabla[1:]
        columnas = []
        for i, conjunto in enumerate(conjunto_filas):
            lista = string_a_lista_numeros(conjunto)

            if all(numero in numerosCantados for numero in lista):
                codigosGanadores.add((codigo, f"Fila {i + 1}"))
                codigosGanadoresInfo.append((codigo, f"Fila {i + 1}"))

        # Verificar columnas si hay datos válidos en las filas
        if conjunto_filas:
            columnas = [[int(fila.split(',')[j]) for fila in conjunto_filas if fila.strip()] for j in range(len(conjunto_filas[0].split(',')))]

            # Verificar columnas
            for j, columna in enumerate(columnas):
                if all(numero in numerosCantados for numero in columna):
                    codigosGanadores.add((codigo, f"Columna {j + 1}"))
                    codigosGanadoresInfo.append((codigo, f"Columna {j + 1}"))
    # Preparar resultados para la ventana emergente
    resultados = '----- Letras Ganadoras -----\n'
    letras_ganadoras = set()
    codigosN = []
    fila1csv = []
    fila2csv = []
    fila3csv = []
    fila4csv = []
    fila5csv = []
    with open(archivo_csv, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            codigosN.append(row[0])
            fila1csv.append(row[1])
            fila2csv.append(row[2])
            fila3csv.append(row[3])
            fila4csv.append(row[4])
            fila5csv.append(row[5])
    # A
    fila_1A = set()
    fila_3A = set()
    columna_1A = set()
    columna_5A = set()

    for codigo, info in codigosGanadores:
        if info == 'Fila 1':
            fila_1A.add(codigo)
        elif info == 'Fila 3':
            fila_3A.add(codigo)
        elif info == 'Columna 1':
            columna_1A.add(codigo)
        elif info == 'Columna 5':
            columna_5A.add(codigo)

    ganadores = fila_1A.intersection(fila_3A).intersection(columna_1A).intersection(columna_5A)

    if ganadores:
        letras_ganadoras.add("A")
        resultados += f"La tabla tiene la letra A: {ganadores}\n"
    else:
        resultados += "Ningúna tabla tiene la letra A.\n"
    # E
    fila_1E = set()
    fila_3E = set()
    fila_5E = set()
    columna_1E = set()

    for codigo, info in codigosGanadores:
        if info == 'Fila 1':
            fila_1E.add(codigo)
        elif info == 'Fila 3':
            fila_3E.add(codigo)
        elif info == 'Fila 5':
            fila_5E.add(codigo)
        elif info == 'Columna 1':
            columna_1E.add(codigo)

    ganadoresE = fila_1E.intersection(fila_3E).intersection(columna_1E).intersection(fila_5E)

    if ganadoresE:
        letras_ganadoras.add("E")
        resultados += f"La tabla tiene la letra E: {ganadoresE}\n"
    else:
        resultados += "Ningúna tabla tiene la letra E.\n"
    # F
    fila_1F = set()
    fila_3F = set()
    columna_1F = set()

    for codigo, info in codigosGanadores:
        if info == 'Fila 1':
            fila_1F.add(codigo)
        elif info == 'Fila 3':
            fila_3F.add(codigo)
        elif info == 'Columna 1':
            columna_1F.add(codigo)

    ganadoresF = fila_1F.intersection(fila_3F).intersection(columna_1F)

    if ganadoresF:
        letras_ganadoras.add("F")
        resultados += f"La tabla tiene la letra F: {ganadoresF}\n"
    else:
        resultados += "Ningúna tabla tiene la letra F.\n"
 # O
    fila_1O = set()
    fila_5O = set()
    columna_1O = set()
    columna_5O = set()

    for codigo, info in codigosGanadores:
        if info == 'Fila 1':
            fila_1O.add(codigo)
        elif info == 'Fila 5':
            fila_5O.add(codigo)
        elif info == 'Columna 1':
            columna_1O.add(codigo)
        elif info == 'Columna 5':
            columna_5O.add(codigo)

    ganadoresO = fila_1O.intersection(fila_5O).intersection(columna_1O).intersection(columna_5O)

    if ganadoresO:
        letras_ganadoras.add("O")
        resultados += f"La tabla tiene la letra O: {ganadoresO}\n"
    else:
        resultados += "Ningúna tabla tiene la letra O.\n"
    # U
    fila_5U = set()
    columna_1U = set()
    columna_5U = set()

    for codigo, info in codigosGanadores:
        if info == 'Fila 5':
            fila_5U.add(codigo)
        elif info == 'Columna 1':
            columna_1U.add(codigo)
        elif info == 'Columna 5':
            columna_5U.add(codigo)

    ganadoresU = fila_5U.intersection(columna_1U).intersection(columna_5U)

    if ganadoresU:
        letras_ganadoras.add("U")
        resultados += f"La tabla tiene la letra U: {ganadoresU}\n"
    else:
        resultados += "Ningúna tabla tiene la letra U.\n"
    # D
    fila_1D = set()
    fila_5D = set()
    columna_2D = set()
    columna_5D = set()

    for codigo, info in codigosGanadores:
        if info == 'Fila 1':
            fila_1D.add(codigo)
        elif info == 'Fila 5':
            fila_5D.add(codigo)
        elif info == 'Columna 2':
            columna_2D.add(codigo)
        elif info == 'Columna 5':
            columna_5D.add(codigo)

    ganadoresD = fila_1D.intersection(fila_5D).intersection(columna_2D).intersection(columna_5D)

    if ganadoresD:
        letras_ganadoras.add("D")
        resultados += f"La tabla tiene la letra D: {ganadoresD}\n"
    else:
        resultados += "Ningúna tabla tiene la letra D.\n"
    # I
    fila_1I = set()
    fila_5I = set()
    columna_3I = set()

    for codigo, info in codigosGanadores:
        if info == 'Fila 1':
            fila_1I.add(codigo)
        elif info == 'Fila 5':
            fila_5I.add(codigo)
        elif info == 'Columna 3':
            columna_3I.add(codigo)

    ganadoresI = fila_1I.intersection(fila_5I).intersection(columna_3I)

    if ganadoresI:
        letras_ganadoras.add("I")
        resultados += f"La tabla tiene la letra I: {ganadoresI}\n"
    else:
        resultados += "Ningúna tabla tiene la letra I.\n"

    # C
    fila_1C = set()
    fila_5C = set()
    columna_1C = set()

    for codigo, info in codigosGanadores:
        if info == 'Fila 1':
            fila_1C.add(codigo)
        elif info == 'Fila 5':
            fila_5C.add(codigo)
        elif info == 'Columna 1':
            columna_1C.add(codigo)

    ganadoresC = fila_1C.intersection(fila_5C).intersection(columna_1C)

    if ganadoresC:
        letras_ganadoras.add("C")
        resultados += f"La tabla tiene la letra C: {ganadoresC}\n"
    else:
        resultados += "Ningúna tabla tiene la letra C.\n"

    # LL
    tabla_con_numeros_cantadosLL = {}

    # Buscar números en fila 5 y registrar los códigos de las tablas
    for i in range(len(fila5csv)):
        fila5 = [int(num) for num in fila5csv[i].split(',')]
        codigoN = codigosN[i]
        fila5columna2 = fila5[1]
        fila5columna5 = fila5[4]
        if fila5columna2 in numerosCantados and fila5columna5 in numerosCantados:
            tabla_con_numeros_cantadosLL[codigoN] = (fila5columna2, fila5columna5)
            codigosGanadoresInfo.append((codigoN, 'Pos LL'))

    columna_1LL = set()
    columna_4LL = set()

    # Registrar códigos ganadores de las columnas
    for codigo, info in codigosGanadores:
        if info == 'Columna 1':
            columna_1LL.add(codigo)
        elif info == 'Columna 4':
            columna_4LL.add(codigo)

    # Determinar las tablas ganadoras de la letra LL
    ganadoresLL = columna_1LL.intersection(columna_4LL)

    # Verificar si alguna tabla ganadora tiene los números cantados en fila 5
    tablas_ll_con_numeros_cantados = set()
    for codigo in ganadoresLL:
        if codigo in tabla_con_numeros_cantadosLL:
            tablas_ll_con_numeros_cantados.add(codigo)

    # Añadir la letra LL a los resultados solo si ambas condiciones se cumplen simultáneamente
    if tablas_ll_con_numeros_cantados:
        letras_ganadoras.add("LL")
        resultados += f"La tabla tiene la letra LL: {tablas_ll_con_numeros_cantados}\n"
    else:
        resultados += "Ninguna tabla tiene la letra LL.\n"

    # W
    tabla_con_numeros_cantadosW = {}
    # Buscar números en fila 5 y registrar los códigos de las tablas
    for i in range(len(fila4csv)):
        fila4 = [int(num) for num in fila4csv[i].split(',')]
        fila3 = [int(num) for num in fila3csv[i].split(',')]
        fila2 = [int(num) for num in fila2csv[i].split(',')]
        codigoN = codigosN[i]
        fila4columna2 = fila4[1]
        fila4columna4 = fila4[3]
        fila3columna3 = fila3[2]
        fila2columna3 = fila2[2]
        if ((fila4columna2 in numerosCantados) and (fila4columna4 in numerosCantados)
                and (fila3columna3 in numerosCantados) and (fila2columna3 in numerosCantados)):
            tabla_con_numeros_cantadosW[codigoN] = (fila4columna2, fila4columna4, fila3columna3, fila2columna3)
            codigosGanadoresInfo.append((codigoN, 'Pos W'))
    columna_1W = set()
    columna_5W = set()
    nueva_pos_w = set(tabla_con_numeros_cantadosW.keys())
    # Registrar códigos ganadores de las columnas
    for codigo, info in codigosGanadores:
        if info == 'Columna 1':
            columna_1W.add(codigo)
        elif info == 'Columna 5':
            columna_5W.add(codigo)

    # Determinar las tablas ganadoras de la letra LL
    ganadoresW = columna_1W.intersection(columna_5W)
    nueva_ganadores_W = ganadoresW.intersection(nueva_pos_w)

    if nueva_ganadores_W:
        letras_ganadoras.add("W")
        resultados += f"La tabla tiene la letra W: {nueva_ganadores_W}\n"
    else:
        resultados += "Ninguna tabla tiene la letra W.\n"

    # R

    tabla_con_numeros_cantadosR = {}
    # Buscar números en fila 5 y registrar los códigos de las tablas
    for i in range(len(fila4csv)):
        fila1 = [int(num) for num in fila1csv[i].split(',')]
        fila2 = [int(num) for num in fila2csv[i].split(',')]
        fila3 = [int(num) for num in fila3csv[i].split(',')]
        fila4 = [int(num) for num in fila4csv[i].split(',')]
        fila5 = [int(num) for num in fila5csv[i].split(',')]
        codigoN = codigosN[i]
        fila1C2 = fila1[1]
        fila1C3 = fila1[2]
        fila1C4 = fila1[3]

        fila3C2 = fila3[1]
        fila3C3 = fila3[2]
        fila3C4 = fila3[3]

        fila2C4 = fila2[3]
        fila4C3 = fila4[2]
        fila5C4 = fila5[3]
        if ((fila1C2 in numerosCantados) and (fila1C3 in numerosCantados)
                and (fila1C4 in numerosCantados) and (fila3C2 in numerosCantados) and (fila3C3 in numerosCantados)
                and (fila3C4 in numerosCantados) and (fila2C4 in numerosCantados) and (fila4C3 in numerosCantados)
                and (fila5C4 in numerosCantados)):
            tabla_con_numeros_cantadosR[codigoN] = (fila1C2, fila1C3, fila1C4, fila3C2, fila3C3, fila3C4, fila2C4, fila4C3, fila5C4)
            codigosGanadoresInfo.append((codigoN, 'Pos R'))
    columna_1R = set()
    nuevos_codigos_R = set(tabla_con_numeros_cantadosR.keys())

    # Registrar códigos ganadores de las columnas
    for codigo, info in codigosGanadores:
        if info == 'Columna 1':
            columna_1R.add(codigo)

    # Determinar las tablas ganadoras de la letra R
    ganadoresR = columna_1R
    nuevos_ganadores_R = ganadoresR.intersection(nuevos_codigos_R)

    if nuevos_ganadores_R:
        letras_ganadoras.add("R")
        resultados += f"La tabla tiene la letra R: {nuevos_ganadores_R}\n"
    else:
        resultados += "Ninguna tabla tiene la letra R.\n"



    # S

    tabla_con_numeros_cantadosS = {}

    # Buscar números en fila 5 y registrar los códigos de las tablas
    for i in range(len(fila5csv)):
        fila2= [int(num) for num in fila2csv[i].split(',')]
        fila4 = [int(num) for num in fila4csv[i].split(',')]
        codigoN = codigosN[i]
        fila2columna1 = fila2[0]
        fila4columna5 = fila4[4]
        if fila2columna1 in numerosCantados and fila4columna5 in numerosCantados:
            tabla_con_numeros_cantadosS[codigoN] = (fila2columna1, fila4columna5)
            codigosGanadoresInfo.append((codigoN, 'Pos S'))
    nuevos_codigos_S = set(tabla_con_numeros_cantadosS.keys())
    fila_1S = set()
    fila_3S = set()
    fila_5S = set()

    # Registrar códigos ganadores de las columnas
    for codigo, info in codigosGanadores:
        if info == 'Fila 1':
            fila_1S.add(codigo)
        elif info == 'Fila 3':
            fila_3S.add(codigo)
        elif info == 'Fila 5':
            fila_5S.add(codigo)

    # Determinar las tablas ganadoras de la letra LL
    ganadoresS = fila_1S.intersection(fila_3S).intersection(fila_5S)
    nuevos_ganadores_s = ganadoresS.intersection(nuevos_codigos_S)

    if nuevos_ganadores_s:
        letras_ganadoras.add("S")
        resultados += f"La tabla tiene la letra S: {nuevos_ganadores_s}\n"
    else:
        resultados += "Ninguna tabla tiene la letra S.\n"

    # K
    tabla_con_numeros_cantadosK = {}

    # Buscar números en fila 5 y registrar los códigos de las tablas
    for i in range(len(fila5csv)):
        fila1 = [int(num) for num in fila1csv[i].split(',')]
        fila2 = [int(num) for num in fila2csv[i].split(',')]
        fila3 = [int(num) for num in fila3csv[i].split(',')]
        fila4 = [int(num) for num in fila4csv[i].split(',')]
        fila5 = [int(num) for num in fila5csv[i].split(',')]
        codigoN = codigosN[i]
        fila1columna4 = fila1[3]
        fila2columna3 = fila2[2]
        fila3columna2 = fila3[1]
        fila4columna3 = fila4[2]
        fila5columna4 = fila5[3]
        if ((fila1columna4 in numerosCantados) and (fila2columna3 in numerosCantados)
                and (fila3columna2 in numerosCantados) and (fila4columna3 in numerosCantados)
                and (fila5columna4 in numerosCantados)):
            tabla_con_numeros_cantadosK[codigoN] = (
            fila1columna4, fila2columna3, fila3columna2, fila4columna3, fila5columna4)
            codigosGanadoresInfo.append((codigoN, 'Pos K'))

    columna_1K = set()

    nuevos_codigos_K = set(tabla_con_numeros_cantadosK.keys())
    # Registrar códigos ganadores de las columnas
    for codigo, info in codigosGanadores:
        if info == 'Columna 1':
            columna_1K.add(codigo)

    # Determinar las tablas ganadoras de la letra K
    ganadoresK = columna_1K.intersection(tabla_con_numeros_cantadosK.keys())
    nuevos_ganadores_K = ganadoresK.intersection(nuevos_codigos_K)

    # Añadir la letra K a los resultados solo si ambas condiciones se cumplen simultáneamente
    if nuevos_ganadores_K:
        letras_ganadoras.add("K")
        resultados += f"La tabla tiene la letra K: {nuevos_ganadores_K}\n"
    else:
        resultados += "Ninguna tabla tiene la letra K.\n"


    # N
    tabla_con_numeros_cantadosN = {}

    # Buscar números en fila 5 y registrar los códigos de las tablas
    for i in range(len(fila5csv)):
        fila2= [int(num) for num in fila2csv[i].split(',')]
        fila3 = [int(num) for num in fila3csv[i].split(',')]
        fila4 = [int(num) for num in fila4csv[i].split(',')]
        codigoN = codigosN[i]
        fila2columna2 = fila2[1]
        fila3columna3 = fila3[2]
        fila4columna4 = fila4[3]
        if ((fila2columna2 in numerosCantados) and (fila3columna3 in numerosCantados) and (fila4columna4 in numerosCantados)):

            tabla_con_numeros_cantadosN[codigoN] = (fila2columna2, fila3columna3, fila4columna4)
            codigosGanadoresInfo.append((codigoN, 'Pos N'))
    conjuntos_claves_N = set(tabla_con_numeros_cantadosN.keys())
    columna_1N = set()
    columna_5N = set()

    # Registrar códigos ganadores de las columnas
    for codigo, info in codigosGanadores:
        if info == 'Columna 1':
            columna_1N.add(codigo)
        elif info == 'Columna 5':
            columna_5N.add(codigo)

    # Determinar las tablas ganadoras de la letra N
    ganadoresN = columna_1N.intersection(columna_5N)
    nuevo_conjuntoN = ganadoresN.intersection(conjuntos_claves_N)

    if nuevo_conjuntoN:
        letras_ganadoras.add("N")
        resultados += f"La tabla tiene la letra N: {nuevo_conjuntoN}\n"
    else:
        resultados += "Ninguna tabla tiene la letra N.\n"

    # Z
    tabla_con_numeros_cantadosZ = {}

    # Buscar números en fila 5 y registrar los códigos de las tablas
    for i in range(len(fila5csv)):
        fila1 = [int(num) for num in fila1csv[i].split(',')]
        fila2 = [int(num) for num in fila2csv[i].split(',')]
        fila3 = [int(num) for num in fila3csv[i].split(',')]
        fila4 = [int(num) for num in fila4csv[i].split(',')]
        fila5 = [int(num) for num in fila5csv[i].split(',')]
        codigoN = codigosN[i]
        fila2columna4 = fila2[3]
        fila3columna3 = fila3[2]
        fila4columna2 = fila4[1]


        # Verificar si las filas 1 y 5 y las posiciones Z están en los números cantados
        if ((fila2columna4 in numerosCantados) and (fila3columna3 in numerosCantados) and (fila4columna2 in numerosCantados)):
            tabla_con_numeros_cantadosZ[codigoN] = (fila2columna4, fila3columna3, fila4columna2)
            codigosGanadoresInfo.append((codigoN, 'Pos Z'))

    conjunto_claves_z = set(tabla_con_numeros_cantadosZ.keys())
    # Registrar códigos ganadores de las filas
    fila_1Z = set()
    fila_5Z = set()

    for codigo, info in codigosGanadores:
        if info == 'Fila 1':
            fila_1Z.add(codigo)
        elif info == 'Fila 5':
            fila_5Z.add(codigo)

    # Determinar las tablas ganadoras de la letra Z
    ganadoresZ = fila_1Z.intersection(fila_5Z)
    nuevoConjuntoZ = conjunto_claves_z.intersection(ganadoresZ)

    # Añadir la letra Z a los resultados solo si ambas condiciones se cumplen simultáneamente
    if nuevoConjuntoZ:
        letras_ganadoras.add("Z")
        resultados += f"La tabla tiene la letra Z: {nuevoConjuntoZ}\n"
    else:
        resultados += "Ninguna tabla tiene la letra Z.\n"

    # LLena
    fila_1LLENA = set()
    fila_2LLENA = set()
    fila_3LLENA = set()
    fila_4LLENA = set()
    fila_5LLENA = set()

    for codigo, info in codigosGanadores:
        if info == 'Fila 1':
            fila_1LLENA.add(codigo)
        elif info == 'Fila 2':
            fila_2LLENA.add(codigo)
        elif info == 'Fila 3':
            fila_3LLENA.add(codigo)
        elif info == 'Fila 4':
            fila_4LLENA.add(codigo)
        elif info == 'Fila 5':
            fila_5LLENA.add(codigo)

    ganadoresLLENA = fila_1LLENA.intersection(fila_2LLENA).intersection(fila_3LLENA).intersection(fila_4LLENA).intersection(fila_5LLENA)

    if ganadoresLLENA:
        letras_ganadoras.add("Llena")
        resultados += f"La tabla tiene la tabla llena: {ganadoresLLENA}\n"
    else:
        resultados += "Ningúna tabla tiene la tabla llena.\n"


    # Cerrar la ventana anterior si existe
    if ventana_resultados is not None:
        ventana_resultados.destroy()

    guardar_en_csv(codigosGanadoresInfo, rutaCSVDeTablasGanadoras)

    # Mostrar resultados en una nueva ventana emergente con barra de desplazamiento
    ventana_resultados = tk.Toplevel(menu)
    ventana_resultados.title("Resultados BingoStar")
    ventana_resultados.iconbitmap(rutaIco)

    # Definir la posición deseada de la ventana
    # Por ejemplo, centrada en la pantalla
    window_width = 600
    window_height = 400
    screen_width = ventana_resultados.winfo_screenwidth()
    screen_height = ventana_resultados.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    geometry_string = f"{window_width}x{window_height}+{x}+{y}"
    ventana_resultados.geometry(geometry_string)

    text_widget = tk.Text(ventana_resultados, wrap='word')
    text_widget.insert('1.0', resultados)
    text_widget.config(state=tk.DISABLED)

    scrollbar = ttk.Scrollbar(ventana_resultados, command=text_widget.yview)
    text_widget['yscrollcommand'] = scrollbar.set

    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


def verificar_codigo_tabla():
    codigo_a_revisar = str(entrada_codigo.get())
    codigosConInfo = []

    # Leer datos del archivo CSV
    with open(rutaCSVDeTablasGanadoras, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            codigosConInfo.append(row[0])

    # Crear estructuras para almacenar códigos y descripciones
    codigosConInfoset = set(codigosConInfo)
    codigosConInfoPuros = list(codigosConInfoset)
    codigo_descripciones = {}

    # Definir etiquetas para filas y columnas
    C1 = 'Columna 1'
    C2 = 'Columna 2'
    C3 = 'Columna 3'
    C4 = 'Columna 4'
    C5 = 'Columna 5'
    F1 = 'Fila 1'
    F2 = 'Fila 2'
    F3 = 'Fila 3'
    F4 = 'Fila 4'
    F5 = 'Fila 5'
    PLL = 'Pos LL'
    PW = 'Pos W'
    PR = 'Pos R'
    PS = 'Pos S'
    PK = 'Pos K'
    PN = 'Pos N'
    PZ = 'Pos Z'
    # Procesar los datos para crear el diccionario de códigos y descripciones
    for dato in codigosConInfoPuros:
        codigo, descripcion = dato.split(',')

        if codigo not in codigo_descripciones:
            codigo_descripciones[codigo] = []

        codigo_descripciones[codigo].append(descripcion.strip())  # Asegúrate de quitar espacios en blanco

    # Verificar si el código está en el diccionario
    if codigo_a_revisar in codigo_descripciones:
        descripciones = set(codigo_descripciones[codigo_a_revisar])  # Convierte a conjunto si aún no lo es

        resultados = []
        if {F1, F3, C1, C5}.issubset(descripciones):  # Usa issubset para verificar la subconjunción
            resultados.append("La Tabla forma la letra A")
        if {F1, F5, C1, C5}.issubset(descripciones):  # Usa issubset para verificar la subconjunción
            resultados.append("La Tabla forma la letra O")
        if {C1, C4, PLL}.issubset(descripciones):  # Usa issubset para verificar la subconjunción
            resultados.append("La Tabla forma la letra LL")
        if {C1, C5, PW}.issubset(descripciones):  # Usa issubset para verificar la subconjunción
            resultados.append("La Tabla forma la letra W")
        if {C1, PR}.issubset(descripciones):  # Usa issubset para verificar la subconjunción
            resultados.append("La Tabla forma la letra R")
        if {F1, F5, C1}.issubset(descripciones):  # Usa issubset para verificar la subconjunción
            resultados.append("La Tabla forma la letra C")
        if {C1, C5, F5}.issubset(descripciones):  # Usa issubset para verificar la subconjunción
            resultados.append("La Tabla forma la letra U")
        if {C1, F1, F3, F5}.issubset(descripciones):  # Usa issubset para verificar la subconjunción
            resultados.append("La Tabla forma la letra E")
        if {C1, F1, F3}.issubset(descripciones):  # Usa issubset para verificar la subconjunción
            resultados.append("La Tabla forma la letra F")
        if {C3, F1, F5}.issubset(descripciones):  # Usa issubset para verificar la subconjunción
            resultados.append("La Tabla forma la letra I")
        if {F1, F5, C2, C5}.issubset(descripciones):  # Usa issubset para verificar la subconjunción
            resultados.append("La Tabla forma la letra D")
        if {F1, F3, F5, PS}.issubset(descripciones):  # Usa issubset para verificar la subconjunción
            resultados.append("La Tabla forma la letra S")
        if {C1, PK}.issubset(descripciones):  # Usa issubset para verificar la subconjunción
            resultados.append("La Tabla forma la letra K")
        if {C1, C5,PN}.issubset(descripciones):  # Usa issubset para verificar la subconjunción
            resultados.append("La Tabla forma la letra N")
        if {F1, F5,PZ}.issubset(descripciones):  # Usa issubset para verificar la subconjunción
            resultados.append("La Tabla forma la letra Z")
        if {F1, F2, F3, F4, F5}.issubset(descripciones):  # Usa issubset para verificar la subconjunción
            resultados.append("Tabla llena")
        resultado_codigo.set("\n".join(resultados))

    else:
        resultado_codigo.set(f"No hay información para el código {codigo_a_revisar}")


# Rutas

rutaCSVDeTablas = 'C:/Users/ferof/OneDrive/Desktop/BingoStarDist/BufferBorrarSoloElContenido/Tablas.csv'
rutaCSVDeTablasGanadoras = 'C:/Users/ferof/OneDrive/Desktop/BingoStarDist/BufferBorrarSoloElContenido/TablasGanadoras.csv'
rutaIco = 'C:/Users/ferof/OneDrive/Desktop/BingoStarDist/Imagenes/CompanyLogo.ico'
rutaPenege = 'C:/Users/ferof/OneDrive/Desktop/BingoStarDist/Imagenes/CompanyLogo.png'
rutaCSVDeTablasWord = 'C:/Users/ferof/OneDrive/Desktop/BingoStarDist/BufferBorrarSoloElContenido/TablasImprimir.docx'

lista_path = [rutaCSVDeTablas, rutaCSVDeTablasGanadoras, rutaCSVDeTablasWord]
numerosCantados = []
ventana_resultados = None
menu = tk.Tk()
menu.title('BingoStar 1.0')
menu.geometry('340x400+1100+230')
menu.iconbitmap(rutaIco)
archivo_csv = rutaCSVDeTablas

filas = []
with open(archivo_csv, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        filas.append(row)

# Crear botones para números del 1 al 99
numeros_frame = tk.Frame(menu)
numeros_frame.place(x=10, y=10)

botones_numeros = []
for numero in range(1, 100):
    boton_numero = tk.Button(numeros_frame, text=str(numero), width=3, command=lambda num=numero: agregar_numero(num))
    boton_numero.grid(row=(numero - 1) // 10, column=(numero - 1) % 10)
    botones_numeros.append(boton_numero)

# Botón para revertir el último número ingresado
boton_revertir = tk.Button(menu, text="Revertir Último Número", command=revertir_ultimo_numero)
boton_revertir.place(x=10, y=320)

boton_borrar = tk.Button(menu, text="Borrar Archivos", command=confirmar_borrado)
boton_borrar.place(x=10, y=360)


# Ventana para ingresar código de tabla y verificar
ventana_verificar = tk.Toplevel(menu)
ventana_verificar.title("Verificar Código de Tabla")
ventana_verificar.geometry('400x200+50+300')


ventana_verificar.iconbitmap(rutaIco)
label_codigo = tk.Label(ventana_verificar, text="Ingrese el código de la tabla:")
label_codigo.pack(pady=10)
label_longitud_numeros = tk.Label(menu, text=f"Longitud de números cantados: {len(numerosCantados)}")
label_longitud_numeros.place(x=10, y=290)
entrada_codigo = tk.Entry(ventana_verificar)
entrada_codigo.pack(pady=10)
boton_verificar_codigo = tk.Button(ventana_verificar, text="Verificar", command=verificar_codigo_tabla)
boton_verificar_codigo.pack(pady=10)
resultado_codigo = tk.StringVar()
label_resultado_codigo = tk.Label(ventana_verificar, textvariable=resultado_codigo)
label_resultado_codigo.pack(pady=10)
# Configuración adicional de la interfaz
Company = tk.Label(menu, text='Software Desarrollado por: RedStar Developers ✫', font=('Times', 10))
Company.place(x=10, y=270)
CompanyPhoto = tk.PhotoImage(file=rutaPenege)
CompanyPhotoPantalla = tk.Label(menu, image=CompanyPhoto)
CompanyPhotoPantalla.place(x=200, y=290)
actualizar_longitud_numeros()
menu.mainloop()