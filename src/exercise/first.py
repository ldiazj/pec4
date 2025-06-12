"""
Módulo del primer ejercicio

Este modulo contiene las funciones para la solución del primer ejercicio
"""
import pandas as pd

def load_file():
    """
    Función para cargar un fichero en un dataframe de Pandas

    Returns:
        dataframe: Dataframe creado desde el fichero
    """
    print("1.1. Cargar el dataset en un dataframe de Pandas")
    return pd.read_csv("doc/dataset.csv")

def show_first_5_rows(df):
    """
    Función para mostrar las 5 primeras filas

    Args:
        df (dataframe): Dataframe sobre el que mostrar la información
    """
    print("1.2. Mostrar las 5 primeras filas")
    print(df.head(5))

def show_columns(df):
    """
    Función para mostrar los nombres de las columnas

    Args:
        df (dataframe): Dataframe sobre el que mostrar la información
    """
    print("1.2. Mostrar las columnas del dataframe")
    print(df.columns)

def show_info(df):
    """
    Función para mostrar la información que devuelve la función info()

    Args:
        df (dataframe): Dataframe sobre el que mostrar la información
    """
    print("1.3. Mostrar la información (info())")
    print(df.info())

def run():
    """
    Función principal para ejecutar el ejercicio 1

    Returns:
        dataframe: Dataframe creado en el ejercicio 1
    """
    print("First Exercise")
    df = load_file()
    show_first_5_rows(df)
    show_columns(df)
    show_info(df)
    return df
