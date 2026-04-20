# Aplicación realizada por Rodrigo Moreno Bielsa

import streamlit as st
import pandas as pd
import joblib


# CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="EcoDrive AI",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)


# CARGAR MODELO
model = joblib.load("modelo_co2.pkl")


# ESTILOS PERSONALIZADOS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0a1f17 0%, #174c34 45%, #2d6a4f 100%);
        color: white;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    h1, h2, h3, h4, h5, h6, p, label, div {
        color: white !important;
    }

    .main-title {
        font-size: 3.4rem;
        font-weight: 800;
        margin-bottom: 0.4rem;
        text-align: center;
        letter-spacing: 0.5px;
    }

    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #d8f3dc !important;
        margin-bottom: 1.2rem;
    }

    .hero-box {
        background: transparent;
        border: none;
        padding: 10px 10px 20px 10px;
        margin-bottom: 10px;
        box-shadow: none;
    }

    .section-card {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255,255,255,0.10);
        backdrop-filter: blur(10px);
        border-radius: 22px;
        padding: 14px;
        box-shadow: 0 6px 25px rgba(0,0,0,0.18);
        margin-bottom: 20px;
    }

    .result-card {
        background: linear-gradient(135deg, #63c29a 0%, #42936d 100%);
        border-radius: 28px;
        padding: 14px 24px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.22);
        border: 1px solid rgba(255,255,255,0.15);
        margin-top: 10px;
        margin-bottom: 20px;
    }

    .result-number {
        font-size: 12.6rem;
        font-weight: 1400;
        margin: 0;
        line-height: 3.1;
        color: white !important;
    }

    .result-label {
        font-size: 1.5rem;
        color: #eefaf2 !important;
        margin-top: 0.7rem;
        font-weight: 600;
    }

    .impact-low {
        background: linear-gradient(135deg, #5cae87 0%, #4b9472 100%);
        color: white;
        font-weight: 700;
        text-align: center;
        border-radius: 20px;
        padding: 16px;
        margin-top: 14px;
        font-size: 1.08rem;
        border: 1px solid rgba(255,255,255,0.10);
    }

    .impact-medium {
        background: linear-gradient(135deg, #c8b26a 0%, #b89b57 100%);
        color: white;
        font-weight: 700;
        text-align: center;
        border-radius: 20px;
        padding: 16px;
        margin-top: 14px;
        font-size: 1.08rem;
        border: 1px solid rgba(255,255,255,0.10);
    }

    .impact-high {
        background: linear-gradient(135deg, #b77979 0%, #a96363 100%);
        color: white;
        font-weight: 700;
        text-align: center;
        border-radius: 20px;
        padding: 16px;
        margin-top: 14px;
        font-size: 1.08rem;
        border: 1px solid rgba(255,255,255,0.10);
    }

    .impact-message {
        border-radius: 20px;
        padding: 18px 20px;
        margin-top: 12px;
        font-size: 1.03rem;
        border: 1px solid rgba(255,255,255,0.08);
        text-align: center;
    }

    .impact-message-low {
        background: rgba(94, 145, 113, 0.85);
        color: white !important;
    }

    .impact-message-medium {
        background: rgba(182, 155, 92, 0.85);
        color: white !important;
    }

    .impact-message-high {
        background: rgba(165, 102, 102, 0.85);
        color: white !important;
    }

    .mini-info {
        border-radius: 18px;
        padding: 18px;
        text-align: center;
        margin-top: 12px;
        border: 1px solid rgba(255,255,255,0.10);
        font-weight: 600;
    }

    .mini-low {
        background: rgba(94, 145, 113, 0.85);
    }

    .mini-medium {
        background: rgba(182, 155, 92, 0.85);
    }

    .mini-high {
        background: rgba(165, 102, 102, 0.85);
    }

    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #95d5b2 0%, #52b788 50%, #40916c 100%);
        color: #081c15 !important;
        border: none;
        border-radius: 14px;
        padding: 0.9rem 1rem;
        font-size: 1.05rem;
        font-weight: 800;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    }

    .stButton > button:hover {
        transform: scale(1.01);
        transition: 0.2s ease-in-out;
        color: #081c15 !important;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0b1d16 0%, #163126 100%);
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    .sidebar-title {
        font-size: 1.4rem;
        font-weight: 800;
        margin-bottom: 0.3rem;
    }

    .sidebar-text {
        color: #d8f3dc !important;
        font-size: 0.95rem;
        margin-bottom: 1rem;
    }

    [data-testid="stMetric"] {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.10);
        padding: 16px;
        border-radius: 18px;
    }

    .footer-note {
        text-align: center;
        color: #edf7f0 !important;
        margin-top: 30px;
        font-size: 1rem;
        padding: 20px;
        background: rgba(18, 58, 43, 0.75);
        border: 1px solid rgba(255,255,255,0.10);
    }
</style>
""", unsafe_allow_html=True)


# CABECERA
st.markdown('<div class="hero-box">', unsafe_allow_html=True)
st.markdown('<div class="main-title">EcoDrive AI</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Calculadora inteligente de emisiones de CO₂ para apoyar decisiones de movilidad más sostenibles</div>',
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)


# SIDEBAR
with st.sidebar:
    st.markdown('<div class="sidebar-title">Configuración del vehículo</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sidebar-text">Introduce los datos técnicos del vehículo y obtenga una estimación de sus emisiones.</div>',
        unsafe_allow_html=True
    )

    vehicle_class = st.selectbox(
        "Clase del vehículo",
        [
            "COMPACT", "SUV - SMALL", "SUV - STANDARD", "MID-SIZE",
            "TWO-SEATER", "MINICOMPACT", "SUBCOMPACT", "STATION WAGON - SMALL",
            "STATION WAGON - MID-SIZE", "FULL-SIZE", "PICKUP TRUCK - SMALL",
            "PICKUP TRUCK - STANDARD", "VAN - CARGO", "VAN - PASSENGER",
            "MINIVAN", "SPECIAL PURPOSE VEHICLE"
        ]
    )

    engine_size = st.number_input(
        "Tamaño del motor (L)",
        min_value=0.8, max_value=10.0, value=2.0, step=0.1
    )

    cylinders = st.number_input(
        "Número de cilindros",
        min_value=2, max_value=16, value=4, step=1
    )

    transmission = st.selectbox(
        "Transmisión",
        [
            "A4", "A5", "A6", "A7", "A8", "A9", "A10",
            "AS4", "AS5", "AS6", "AS7", "AS8", "AS9", "AS10",
            "M5", "M6", "AV", "AM7", "AM8"
        ]
    )

    fuel_type = st.selectbox(
        "Tipo de combustible",
        ["X", "Z", "D", "E", "N"]
    )

    fuel_city = st.number_input(
        "Consumo en ciudad (L/100 km)",
        min_value=0.0, max_value=40.0, value=10.0, step=0.1
    )

    fuel_hwy = st.number_input(
        "Consumo en carretera (L/100 km)",
        min_value=0.0, max_value=30.0, value=7.0, step=0.1
    )

    fuel_comb = st.number_input(
        "Consumo combinado (L/100 km)",
        min_value=0.0, max_value=35.0, value=8.5, step=0.1
    )

    fuel_mpg = st.number_input(
        "Consumo combinado (mpg)",
        min_value=0.0, max_value=100.0, value=33.0, step=1.0
    )

    predict_button = st.button("Calcular emisiones")


# DATOS DE ENTRADA
input_data = pd.DataFrame([{
    "Vehicle Class": vehicle_class,
    "Engine Size(L)": engine_size,
    "Cylinders": cylinders,
    "Transmission": transmission,
    "Fuel Type": fuel_type,
    "Fuel Consumption City (L/100 km)": fuel_city,
    "Fuel Consumption Hwy (L/100 km)": fuel_hwy,
    "Fuel Consumption Comb (L/100 km)": fuel_comb,
    "Fuel Consumption Comb (mpg)": fuel_mpg
}])


# RESULTADOS ARRIBA
if predict_button:
    prediction = model.predict(input_data)[0]

    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown(
    f"""
    <div style="font-size:48px; font-weight:bold;">
        {prediction:.2f} g/km
    </div>
    <div style="font-size:20px; opacity:0.8;">
        Emisiones estimadas de CO₂
    </div>
    """,
    unsafe_allow_html=True
)
    st.markdown('</div>', unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Motor", f"{engine_size:.1f} L")
    with m2:
        st.metric("Cilindros", f"{int(cylinders)}")
    with m3:
        st.metric("Consumo combinado", f"{fuel_comb:.1f} L/100 km")

    if prediction < 150:
        st.markdown('<div class="impact-low">Impacto medioambiental bajo</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="impact-message impact-message-low">Este vehículo presenta unas emisiones relativamente reducidas dentro de la escala definida en la aplicación.</div>',
            unsafe_allow_html=True
        )
    elif prediction < 250:
        st.markdown('<div class="impact-medium">Impacto medioambiental medio</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="impact-message impact-message-medium">Este vehículo presenta un nivel intermedio de emisiones. Puede haber alternativas más sostenibles.</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown('<div class="impact-high">Impacto medioambiental alto</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="impact-message impact-message-high">Este vehículo presenta unas emisiones elevadas y un mayor impacto medioambiental.</div>',
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)


# INFORMACIÓN SECUNDARIA ABAJO
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("Resumen del vehículo")
    st.write("Los datos seleccionados para la simulación actual son los siguientes:")

    preview_df = pd.DataFrame({
        "Característica": [
            "Clase",
            "Motor (L)",
            "Cilindros",
            "Transmisión",
            "Combustible",
            "Consumo ciudad",
            "Consumo carretera",
            "Consumo combinado",
            "Consumo combinado (mpg)"
        ],
        "Valor": [
            vehicle_class,
            engine_size,
            cylinders,
            transmission,
            fuel_type,
            fuel_city,
            fuel_hwy,
            fuel_comb,
            fuel_mpg
        ]
    })

    st.dataframe(preview_df, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("Interpretación orientativa")
    st.write("La aplicación clasifica el resultado en tres niveles para facilitar su lectura:")

    st.markdown('<div class="mini-info mini-low"><b>Menos de 150 g/km</b><br>Impacto bajo</div>', unsafe_allow_html=True)
    st.markdown('<div class="mini-info mini-medium"><b>Entre 150 y 250 g/km</b><br>Impacto medio</div>', unsafe_allow_html=True)
    st.markdown('<div class="mini-info mini-high"><b>Más de 250 g/km</b><br>Impacto alto</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# PIE
st.markdown(
    '<div class="footer-note">Proyecto de Machine Learning aplicado en medio ambiente y sostenibilidad - Por Rodrigo Moreno Bielsa para el IES Maestre de Calatrava</div>',
    unsafe_allow_html=True
)