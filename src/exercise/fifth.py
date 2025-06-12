"""
Módulo del quinto ejercicio

Este modulo contiene las funciones para la solución del quinto ejercicio
"""
def calculate_periods(df):
    """
    Función para calcular los periodos del sequía

    Args:
        df (dataframe): Dataframe sobre el que se obtienen los periodos

    Returns:
        array: Lista de los periodos de sequía
    """
    periods = []
    start_date = None

    for row in df.itertuples():
        if row.nivell_perc_smooth <= 60:
            if start_date is None:
                start_date = round(row.dia_decimal, 2)
        else:
            if start_date is not None:
                end_date = round(row.dia_decimal, 2)
                periods.append([start_date, end_date])
                start_date = None

    if start_date is not None:
        end_date = round(df.loc[len(df)-1, 'dia_decimal'], 2)
        periods.append([start_date, end_date])

    return periods

def run(df):
    """
    Función principal para ejecutar el ejercicio 5

    Args:
        df (dataframe): Dataframe sobre el que trabajar
    """
    print("Fifth Exercise")
    print("5.1. Definir la función calculate_periods()")
    print("5.2. Ejecutar función y printar resultado")
    print(f'Periodos de sequía: {calculate_periods(df)}')
