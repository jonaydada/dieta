import streamlit as st

# Configuración de la página para móviles
st.set_page_config(page_title="Control Nutricional", page_icon="💪", layout="centered")

# Base de datos nutricional (Valores por cada 100 gramos)
TABLA_NUTRICIONAL = {
    "pechuga de pollo": {"calorias": 165, "proteina": 31.0},
    "muslo de pollo sin piel": {"calorias": 209, "proteina": 26.0},
    "pavo (pechuga)": {"calorias": 135, "proteina": 30.0},
    "ternera magra": {"calorias": 170, "proteina": 26.0},
    "solomillo de ternera": {"calorias": 190, "proteina": 27.0},
    "lomo de cerdo": {"calorias": 143, "proteina": 26.0},
    "jamon cocido": {"calorias": 116, "proteina": 20.0},
    "jamon serrano": {"calorias": 241, "proteina": 31.0},
    "conejo": {"calorias": 173, "proteina": 33.0},
    "cordero magro": {"calorias": 206, "proteina": 25.0},
    "atun al natural": {"calorias": 116, "proteina": 26.0},
    "salmon": {"calorias": 208, "proteina": 20.0},
    "merluza": {"calorias": 82, "proteina": 18.0},
    "bacalao": {"calorias": 82, "proteina": 18.0},
    "sardinas": {"calorias": 208, "proteina": 25.0},
    "caballa": {"calorias": 205, "proteina": 19.0},
    "dorada": {"calorias": 96, "proteina": 20.0},
    "lubina": {"calorias": 97, "proteina": 19.0},
    "gambas": {"calorias": 99, "proteina": 24.0},
    "mejillones": {"calorias": 86, "proteina": 12.0},
    "huevos enteros": {"calorias": 143, "proteina": 13.0},
    "claras de huevo": {"calorias": 52, "proteina": 11.0},
    "leche desnatada": {"calorias": 35, "proteina": 3.5},
    "leche semidesnatada": {"calorias": 46, "proteina": 3.3},
    "leche entera": {"calorias": 61, "proteina": 3.2},
    "yogur griego 0%": {"calorias": 59, "proteina": 10.0},
    "yogur natural": {"calorias": 61, "proteina": 3.5},
    "queso fresco batido 0%": {"calorias": 45, "proteina": 8.0},
    "requeson": {"calorias": 98, "proteina": 11.0},
    "queso cottage": {"calorias": 98, "proteina": 11.0},
    "mozzarella light": {"calorias": 200, "proteina": 24.0},
    "queso curado": {"calorias": 400, "proteina": 25.0},
    "parmesano": {"calorias": 431, "proteina": 38.0},
    "skyr": {"calorias": 63, "proteina": 11.0},
    "kefir": {"calorias": 60, "proteina": 3.5},
    "tofu firme": {"calorias": 144, "proteina": 17.0},
    "tempeh": {"calorias": 193, "proteina": 20.0},
    "soja texturizada seca": {"calorias": 330, "proteina": 50.0},
    "edamame": {"calorias": 121, "proteina": 11.0},
    "seitan": {"calorias": 143, "proteina": 25.0},
    "lentejas cocidas": {"calorias": 116, "proteina": 9.0},
    "garbanzos cocidos": {"calorias": 164, "proteina": 9.0},
    "alubias cocidas": {"calorias": 127, "proteina": 9.0},
    "guisantes": {"calorias": 81, "proteina": 5.0},
    "habas": {"calorias": 88, "proteina": 8.0},
    "quinoa cocida": {"calorias": 120, "proteina": 4.0},
    "arroz blanco cocido": {"calorias": 130, "proteina": 2.7},
    "arroz integral cocido": {"calorias": 111, "proteina": 2.6},
    "pasta cocida": {"calorias": 158, "proteina": 5.8},
    "avena": {"calorias": 389, "proteina": 17.0},
    "pan integral": {"calorias": 247, "proteina": 13.0},
    "pan blanco": {"calorias": 265, "proteina": 9.0},
    "tortillas de trigo": {"calorias": 310, "proteina": 8.0},
    "couscous cocido": {"calorias": 112, "proteina": 3.8},
    "mijo cocido": {"calorias": 119, "proteina": 3.5},
    "trigo sarraceno cocido": {"calorias": 92, "proteina": 3.4},
    "patata cocida": {"calorias": 87, "proteina": 2.0},
    "batata": {"calorias": 86, "proteina": 1.6},
    "maiz dulce": {"calorias": 96, "proteina": 3.4},
    "aguacate": {"calorias": 160, "proteina": 2.0},
    "almendras": {"calorias": 579, "proteina": 21.0},
    "nueces": {"calorias": 654, "proteina": 15.0},
    "pistachos": {"calorias": 562, "proteina": 20.0},
    "anacardos": {"calorias": 553, "proteina": 18.0},
    "avellanas": {"calorias": 628, "proteina": 15.0},
    "cacahuetes": {"calorias": 567, "proteina": 26.0},
    "crema de cacahuete": {"calorias": 588, "proteina": 25.0},
    "semillas de chia": {"calorias": 486, "proteina": 17.0},
    "semillas de lino": {"calorias": 534, "proteina": 18.0},
    "semillas de calabaza": {"calorias": 559, "proteina": 30.0},
    "aceite de oliva": {"calorias": 884, "proteina": 0.0},
    "aceitunas": {"calorias": 145, "proteina": 1.0},
    "brocoli": {"calorias": 34, "proteina": 2.8},
    "espinacas": {"calorias": 23, "proteina": 2.9},
    "coliflor": {"calorias": 25, "proteina": 2.0},
    "zanahoria": {"calorias": 41, "proteina": 0.9},
    "tomate": {"calorias": 18, "proteina": 0.9},
    "pepino": {"calorias": 15, "proteina": 0.7},
    "pimiento rojo": {"calorias": 31, "proteina": 1.0},
    "cebolla": {"calorias": 40, "proteina": 1.1},
    "champiñones": {"calorias": 22, "proteina": 3.1},
    "calabacin": {"calorias": 17, "proteina": 1.2},
    "lechuga": {"calorias": 15, "proteina": 1.4},
    "esparragos": {"calorias": 20, "proteina": 2.2},
    "judias verdes": {"calorias": 31, "proteina": 1.8},
    "manzana": {"calorias": 52, "proteina": 0.3},
    "platano": {"calorias": 89, "proteina": 1.1},
    "naranja": {"calorias": 47, "proteina": 0.9},
    "mandarina": {"calorias": 53, "proteina": 0.8},
    "pera": {"calorias": 57, "proteina": 0.4},
    "fresas": {"calorias": 32, "proteina": 0.7},
    "uvas": {"calorias": 69, "proteina": 0.7},
    "piña": {"calorias": 50, "proteina": 0.5},
    "mango": {"calorias": 60, "proteina": 0.8},
    "kiwi": {"calorias": 61, "proteina": 1.1},
    "sandia": {"calorias": 30, "proteina": 0.6},
    "datiles": {"calorias": 282, "proteina": 2.5},
    "chocolate negro 85%": {"calorias": 600, "proteina": 8.0},
    "proteina whey": {"calorias": 390, "proteina": 80.0},
    "miel": {"calorias": 304, "proteina": 0.2},
    "harina de trigo": {"calorias": 364, "proteina": 10.0}
}

# Inicializar el estado de la aplicación para guardar las comidas del día
if "registro_diario" not in st.session_state:
    st.session_state.registro_diario = {
        "Desayuno": [],
        "Almuerzo": [],
        "Merienda": [],
        "Cena": []
    }

st.title("🍎 Mi Diario Nutricional")
st.write("Registra tus comidas y calcula tus calorías y proteínas diarias al instante.")

# --- FORMULARIO PARA AÑADIR ALIMENTO ---
st.subheader("➕ Añadir Alimento")

comida_seleccionada = st.selectbox("¿A qué comida corresponde?", ["Desayuno", "Almuerzo", "Merienda", "Cena"])
alimento_seleccionado = st.selectbox("Selecciona el alimento", sorted(list(TABLA_NUTRICIONAL.keys())))
gramos = st.number_input("Cantidad consumida (gramos)", min_value=0.0, step=10.0, value=100.0)

if st.button("Agregar Alimento"):
    if gramos > 0:
        # Calcular nutrientes basados en la regla de 3
        cal_100g = TABLA_NUTRICIONAL[alimento_seleccionado]["calorias"]
        prot_100g = TABLA_NUTRICIONAL[alimento_seleccionado]["proteina"]
        
        cal_finales = (gramos * cal_100g) / 100.0
        prot_finales = (gramos * prot_100g) / 100.0
        
        # Guardar en la lista correspondiente
        st.session_state.registro_diario[comida_seleccionada].append({
            "alimento": alimento_seleccionado,
            "gramos": gramos,
            "calorias": cal_finales,
            "proteina": prot_finales
        })
        st.success(f"¡Añadido al {comida_seleccionada}: {gramos}g de {alimento_seleccionado}!")
    else:
        st.error("Por favor, introduce una cantidad mayor a 0 gramos.")

st.markdown("---")

# --- MOSTRAR DESGLOSE POR COMIDAS ---
st.subheader("📊 Desglose del Día")

total_diario_cal = 0.0
total_diario_prot = 0.0

for comida, items in st.session_state.registro_diario.items():
    cal_comida = sum(item["calorias"] for item in items)
    prot_comida = sum(item["proteina"] for item in items)
    
    total_diario_cal += cal_comida
    total_diario_prot += prot_comida
    
    with st.expander(f"{comida} - Subtotal: {cal_comida:.1f} kcal | {prot_comida:.1f}g prot"):
        if len(items) == 0:
            st.write("No has añadido alimentos aún.")
        else:
            for item in items:
                st.write(f"• **{item['alimento']}**: {item['gramos']}g ➔ {item['calorias']:.1f} kcal | {item['proteina']:.1f}g prot")

st.markdown("---")

# --- RESUMEN FINAL DEL DÍA ---
st.subheader("🏆 Total Diario Acumulado")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="🔥 Calorías Totales", value=f"{total_diario_cal:.1f} kcal")
with col2:
    st.metric(label="💪 Proteínas Totales", value=f"{total_diario_prot:.1f} g")

# Botón para resetear el día
if st.button("🗑️ Reiniciar todo el día"):
    st.session_state.registro_diario = {"Desayuno": [], "Almuerzo": [], "Merienda": [], "Cena": []}
    st.rerun()