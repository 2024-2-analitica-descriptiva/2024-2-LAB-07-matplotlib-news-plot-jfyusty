"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import matplotlib.pyplot as plt
import os # Importa os para manejo de rutas y directorios.

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    # Cargamos el archivo CSV
    file_path = 'files/input/news.csv'
    df = pd.read_csv(file_path, index_col=0)

    plt.figure()

    colors = {
        'Television': 'dimgray',
        'Newspaper': 'grey',
        'Internet': 'tab:blue',
        'Radio': 'lightgrey',
    }

    zorder = {
        'Television': 1,
        'Newspaper': 1,
        'Internet': 2,
        'Radio': 1,
    }

    linewidths = {
        'Television': 2,
        'Newspaper': 2,
        'Internet': 4,
        'Radio': 2,
    }

    for col in df.columns:
        plt.plot(df[col],
                color=colors[col],
                label=col,
                zorder=zorder[col],
                linewidth=linewidths[col],
                )

    plt.title("How people get their news", ha='center', va='center', fontsize=16, y=1.05)
    plt.text(0.5, 1, "Una proporción cada vez mayor cita Internet como su principal fuente de noticias",
            ha='center', va='center', transform=plt.gca().transAxes, fontsize=8)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for col in df.columns:
        first_year = df.index[0]
        plt.scatter(
            x=first_year,
            y=df[col][first_year],
            color=colors[col],
            zorder=zorder[col],
        )

        plt.text(
            first_year - 0.2,
            df[col][first_year],
            col +" " +str(df[col][first_year]) + "%",
            ha='right',
            va='center',
            color=colors[col],
        )

        last_year = df.index[-1]
        plt.scatter(
            x=last_year,
            y=df[col][last_year],
            color=colors[col],
        )

        plt.text(
            last_year + 0.2,
            df[col][last_year],
            str(df[col][last_year]) + "%",
            ha='left',
            va='center',
            color=colors[col],
        )

    plt.xticks(
        ticks=df.index,
        labels=df.index,
        ha='center',
    )


    # Crear directorio de salida si no existe
    output_dir = 'files/plots' # Define la carpeta de salida
    os.makedirs(output_dir, exist_ok=True) # Crea la carpeta si no existe.

    plt.savefig(f'{output_dir}/news.png')

# Ejecuta la función para generar el gráfico
pregunta_01()