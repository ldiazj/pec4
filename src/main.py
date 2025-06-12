"""
Módulo principal

Este modulo contiene la función main y el que se ejecuta
"""
import argparse
from exercise import first, second, third, fourth, fifth

def main():
    """
    Función principal que ejecuta los ejercicios en función del parámetro que se pone
    """
    parser = argparse.ArgumentParser(description="Ejecutar ejercicios")
    parser.add_argument("-ex", type=int, help="Ejecutar hasta el ejecicio N", default=None)

    args = parser.parse_args()
    exercise = args.ex

    if exercise is None:
        exercise = 5

    if 1 <= exercise <= 5:
        pec_df = first.run()

        if exercise >= 2:
            pec_df_clean = second.run(pec_df)

            if exercise >= 3:
                pec_df_new_column = third.run(pec_df_clean)

                if exercise >= 4:
                    pec_df_with_smooth = fourth.run(pec_df_new_column)

                    if exercise >= 5:
                        fifth.run(pec_df_with_smooth)
    else:
        print("Número de ejercicio fuera de rango")

if __name__ == "__main__":
    main()
