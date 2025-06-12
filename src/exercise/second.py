"""
Módulo del segundo ejercicio

Este modulo contiene las funciones para la solución del segundo ejercicio
"""
import re

def rename_columns(df):
    """
    Función que, con un diccionario definido, modifica el nombre de las columnas

    Args:
        df (dataframe): Dataframe sobre el que se hace el cambio

    Returns:
        dataframe: Dataframe con las columnas cambiadas de nombre
    """
    print("2.1. Renombrar columnas")
    return df.rename(
        columns={
            "Dia": "dia",
            "Estació": "estacio",
            "Nivell absolut (msnm)": "nivell_msnm",
            "Percentatge volum embassat (%)":
            "nivell_perc",
            "Volum embassat (hm3)": "volum"}
        )

def get_unique_names(df):
    """
    Función que devuelve los valores únicos para la columna 'estacio'

    Args:
        df (dataframe): Dataframe sobre el que se devuelve la información
    
    Returns:
        array: Lista con los nombres de los pantanos
    """
    print("2.2. Mostrar valores únicos del nombre de los pantanos")
    array_names = df['estacio'].unique()
    return array_names.tolist()

def clean_name(embassament):
    """
    Función que limpia un string aplicando una expresión regular

    Args:
        embassament (string): Cadena a limpiar
    
    Returns:
        string: El nombre aplicado la expresion regular
    """
    return re.sub(r'Embassament de |\s*\([^)]*\)', '', embassament)

def rename_names(df):
    """
    Función que renombra los nombres de los pantanos

    Args:
        df (dataframe): Dataframe sobre el que se aplica el cambio
    
    Returns:
        dataframe: Dataframe con la función aplicada
    """
    print("2.3. Renombrar nombre de los pantanos")
    df['estacio'] = df['estacio'].apply(clean_name)
    return df

def filter_by_baells(df):
    """
    Función que filtra el dataframe para solo contener los pantanos de 'la Baells'

    Args:
        df (dataframe): Dataframe sobre el que se filtra
    
    Returns:
        dataframe: Daraframe filtrado
    """
    print("2.4. Dataframe filtrado por los pantanos de 'la Baells'")
    return df.loc[df['estacio'] == 'la Baells']

def run(df):
    """
    Función principal para ejecutar el ejercicio 2

    Args:
        df (dataframe): Dataframe sobre el que trabajar
    
    Returns:
        dataframe: Dataframe modificado en el ejercicio 2
    """
    print("Second Exercise")
    df_renamed_columns = rename_columns(df)
    print(get_unique_names(df_renamed_columns))
    df_renamed_names = rename_names(df_renamed_columns)
    return filter_by_baells(df_renamed_names)
