import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
df = pd.read_csv("vehicles_us.csv")

# Título de la aplicación
st.title("🚀 Dashboard Interactivo de Venta de Autos")

st.sidebar.header("🎛️ Filtros Interactivos")

# Filtro de precio
precio_min, precio_max = st.sidebar.slider(
    "Rango de Precio ($)", 
    min_value=int(df["price"].min()), 
    max_value=int(df["price"].max()), 
    value=(5000, 50000)  # Valores iniciales por defecto
)

# Filtro de año del modelo
year_min, year_max = st.sidebar.slider(
    "Rango de Año del Modelo", 
    min_value=int(df["model_year"].min()), 
    max_value=int(df["model_year"].max()), 
    value=(2000, 2020)  # Valores iniciales por defecto
)

# Filtro de tipo de auto
tipo_auto = st.sidebar.multiselect("Selecciona los tipos de autos:", df["type"].unique(), default=df["type"].unique())

# Aplicar filtros al dataset
df_filtrado = df[
    (df["price"] >= precio_min) & (df["price"] <= precio_max) &
    (df["model_year"] >= year_min) & (df["model_year"] <= year_max) &
    (df["type"].isin(tipo_auto))
]

st.write(f"🔎 Mostrando autos con precio entre **${precio_min}** y **${precio_max}**, y año entre **{year_min}** y **{year_max}**")

st.dataframe(df_filtrado.head())  # Vista previa de los datos filtrados

# 📈 Histograma de precios
st.subheader("📈 Distribución de Precios de los Vehículos (Filtrado)")

fig = px.histogram(df_filtrado, x="price", nbins=50, title="Distribución de Precios de los Vehículos")
st.plotly_chart(fig, use_container_width=True)

# 📊 Gráfico de dispersión Año vs Precio
st.subheader("📊 Relación entre Año del Modelo y Precio (Filtrado)")

fig2 = px.scatter(df_filtrado, x="model_year", y="price", opacity=0.5, title="Año del Modelo vs Precio")
st.plotly_chart(fig2, use_container_width=True)

# Contar cantidad de autos por tipo
conteo_tipos = df_filtrado["type"].value_counts().reset_index()
conteo_tipos.columns = ["Tipo de Auto", "Cantidad"]  # Renombrar columnas correctamente

# Gráfico de barras
fig3 = px.bar(conteo_tipos, 
              x="Tipo de Auto", y="Cantidad", 
              title="Cantidad de Autos por Tipo (Filtrado)",
              labels={"Tipo de Auto": "Tipo de Auto", "Cantidad": "Cantidad"},
              text_auto=True)

st.plotly_chart(fig3, use_container_width=True)

st.markdown("""
    <style>
    /* Fondo sólido sin GIF */
    .main {
        background-color: #f5f7fa; /* Un gris claro limpio */
    }

    /* Ajuste del Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #1e3c72 !important;
        padding: 20px;
    }

    /* Restaurar títulos visibles */
    h1, h2, h3, h4 {
        color: #1e3c72 !important;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
    }

    /* Mejorar los filtros */
    div[data-testid="stSlider"], div[data-testid="stSelectbox"], div[data-testid="stMultiSelect"] {
        background-color: rgba(255, 255, 255, 0.9);
        color: black;
        border-radius: 5px;
    }

    /* Fondos de los gráficos */
    .stPlotlyChart {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 15px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)



st.markdown('<div class="main">', unsafe_allow_html=True)  # Activa el fondo
