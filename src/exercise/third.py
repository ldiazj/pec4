"""
Módulo del tercer ejercicio

Este modulo contiene las funciones para la solución del tercer ejercicio
"""
from datetime import datetime as dt
import time
import pandas as pd
import matplotlib.pyplot as plt

def convert_to_datetime(df):
    """
    Función que convierte la columna 'dia' a tipo datetime

    Args:
        df (dataframe): Dataframe sobre el que se hace la conversión

    Returns:
        dataframe: Dataframe con la conversión en la columna
    """
    print("3.1. Convertir columna dia a datetime")
    df['dia'] = pd.to_datetime(df['dia'], format='%d/%m/%Y')
    return df

def order_by_date(df):
    """
    Función que devuelve el dataframe ordenado por la column 'dia' ascendentemente

    Args:
        df (dataframe): Dataframe sobre el que se aplica el orden
    
    Returns:
        dataframe: Dataframe orenado
    """
    print("3.2. Datos totales, ordenar por día ascendentemente, fecha mas antigua y mas reciente")
    return df.sort_values("dia", ascending=True)

def convert_to_fraction(df):
    """
    Función que añade una columna nueva aplicando la función to_year_fraction en la columna 'dia'

    Args:
        df (dataframe): Dataframe sobre el que se aplica la conversión
    
    Returns:
        dataframe: Dataframe con la columna nueva
    """
    print("3.4. Crear la columna dia_decimal con la función nueva")
    df['dia_decimal'] = df['dia'].apply(to_year_fraction)
    return df

def to_year_fraction(date):
    """
    Función que convierte una fecha en un decimal

    Args:
        date (datetime): Datetime sobre el que se hace la conversión

    Returns:
        float: Decimal con la conversión de la fecha
    """
    def since_epoch(date):
        return time.mktime(date.timetuple())
    s = since_epoch

    year = date.year
    start_of_this_year = dt(year=year, month=1, day=1)
    start_of_next_year = dt(year=year+1, month=1, day=1)

    year_elapsed = s(date) - s(start_of_this_year)
    year_duration = s(start_of_next_year) - s(start_of_this_year)
    fraction = year_elapsed/year_duration

    return date.year + fraction

def create_graph_save_image(df):
    """
    Función que genera un gráfico y lo guarda en una imagen

    Args:
        df (dataframe): Dataframe sobre el que se hace el gráfico
    """
    print("3.5. Crear gráfico con la columna nueva y el porcentaje de volumen")
    plt.figure(figsize=(12,7))

    plt.plot(df['dia_decimal'], df['nivell_perc'])
    plt.suptitle('Tiempo vs Porcentaje', fontsize=14)
    plt.title('Lia Diaz Jimenez', fontsize=9)
    plt.xlabel('Tiempo', fontsize=10)
    plt.ylabel('Porcentaje de volumen', fontsize=10)

    print("3.5. Guardar el gráfico en una imagen")
    plt.savefig('img/labaelles_lia_diaz_jimenez.png')

def run(df):
    """
    Función principal para ejecutar el ejercicio 3

    Args:
        df (dataframe): Dataframe sobre el que trabajar

    Returns:
        dataframe: Dataframe modificado en el ejercicio 3
    """
    print("Third Exercise")
    df_convert = convert_to_datetime(df)
    df_order = order_by_date(df_convert)
    print(f'Datos totales: {len(df_order)}')
    print(f'Fecha más antigua: {df_order['dia'].head(1).iloc[0]}')
    print(f'Fecha más reciente: {df_order['dia'].tail(1).iloc[0]}')
    print("3.3. Definición de la función to_year_fraction()")
    df_new_column = convert_to_fraction(df_order)
    create_graph_save_image(df_new_column)
    return df_new_column
