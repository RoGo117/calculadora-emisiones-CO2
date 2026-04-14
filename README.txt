
**********************
***    ECODRIVE    ***
**********************

Aplicación realizada por Rodrigo Moreno Bielsa
https://github.com/RoGo117/calculadora-emisiones-CO2
----------------------------------------------

- Funcionamiento del programa:
    Este programa permite estimar las emisiones de CO₂ de un vehículo a partir de sus características técnicas.

    El usuario introduce datos como el tipo de vehículo, motor, consumo de combustible, etc., y el sistema devuelve:
    Una estimación de emisiones en g/km
    Una clasificación del impacto medioambiental (bajo, medio o alto)

    El objetivo es concienciar sobre el impacto ambiental de los vehículos y ayudar a tomar decisiones más sostenibles.


- Requisitos:
    pandas
    numpy
    matplotlib
    scikit-learn
    streamlit
    joblib

- Instalación de requisitos:
    Ejecutar el siguiente comando para la instalación de los requisitos:
    
    python -m pip install pandas numpy matplotlib scikit-learn streamlit joblib


- Ejecución del programa
    Ejecutar el siguiente comando para iniciar la aplicación:
    
    python -m streamlit run CalculadoraDeEmisionesRMB.py

(Asegurarse de cumplir con la estructura de archivos correcta)


- Estructura de archivos:
    /Proyecto
    │
    ├── CalculadoraDeEmisionesRMB.py   # Aplicación principal (Streamlit)
    ├── modelo_co2.pkl                 # Modelo entrenado
    ├── CO2_Emissions_Canada.csv       # Dataset principal
    ├── Data_Description.csv           # Descripción de datos
    ├── ProyectoMLRMB.ipynb            # Cuaderno de desarrollo
    └── README.txt                     # Este archivo


- Dataset:
El dataset fue obtenido de kaggle, "CO2 Emission by Vehicles".
https://www.kaggle.com/datasets/debajyotipodder/co2-emission-by-vehicles?


- Tecnologías utilizadas:
    Python → lenguaje principal del proyecto
    pandas → manipulación y procesamiento de datos
    numpy → cálculos numéricos
    matplotlib → visualización de datos para el análisis
    scikit-learn → entrenamiento de modelos de Machine Learning
    joblib → guardado y carga del modelo entrenado (.pkl)
    Streamlit → creación de la aplicación web interactiva

