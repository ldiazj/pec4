"""
Módulo del cuarto ejercicio

Este modulo contiene las funciones para la solución del cuarto ejercicio
"""
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

def add_smooth_save_image(df, window_length, polyorder):
    """
    Función que genera un gráfico, aplica la función savgol_filter y lo guarda en una imagen

    Args:
        df (dataframe): Dataframe sobre el que se hace el grágico
        window_length (int): Parámetro usado en la función savgol_filter
        polyorder (int): Parámetro usado en la función savgol_filter
    
    Returns:
        dataframe: Dataframe con una columna nueva
    """
    print("4.1. Aplicar smoothing")
    df_smooth = savgol_filter(df['nivell_perc'], window_length, polyorder)

    print("4.1.1. Se añade la lista suavizada como columna")
    df["nivell_perc_smooth"] = df_smooth

    print("4.2. Crear gráfico con el smooth")
    plt.figure(figsize=(12,7))

    plt.plot(df['dia_decimal'], df['nivell_perc'])
    plt.plot(df['dia_decimal'], df_smooth, linewidth=3.5, label='smoothed')

    plt.legend()
    plt.suptitle('Embassament de La Baells', fontsize=14)
    plt.title('Lia Diaz Jimenez', fontsize=9)
    plt.xlabel('Tiempo', fontsize=10)
    plt.ylabel('Porcentaje de volumen (%)', fontsize=10)

    print("4.3. Guardar el gráfico en una imagen")
    plt.savefig('img/labaelles_smoothed_lia_diaz_jimenez.png')

    return df

def run(df):
    """
    Función principal para ejecutar el ejercicio 4

    Args:
        df (dataframe): Dataframe sobre el que trabajar

    Returns:
        dataframe: Dataframe modificado en el ejercicio 4
    """
    print("Fourth Exercise")
    return add_smooth_save_image(df, 1500, 3)
