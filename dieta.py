# -*- coding: utf-8 -*-

# Base de datos nutricional (Valores de referencia por cada 100 gramos)
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

def calcular_nutrientes(alimento, gramos):
    """Calcula las calorías y proteínas para una cantidad dada de gramos."""
    datos = TABLA_NUTRICIONAL[alimento]
    calorias_finales = (gramos * datos["calorias"]) / 100.0
    proteinas_finales = (gramos * datos["proteina"]) / 100.0
    return calorias_finales, proteinas_finales

def ejecutar_registro_diario():
    # Estructura diaria de comidas
    comidas = ["Desayuno", "Almuerzo", "Merienda", "Cena"]
    
    # Acumuladores del total del día completo
    total_diario_cal = 0.0
    total_diario_prot = 0.0
    
    print("====================================================")
    print("      SISTEMA DE CONTROL DIARIO NUTRICIONAL         ")
    print("====================================================")
    
    for comida in comidas:
        print(f"\n>>>> Iniciando registro para: {comida} <<<<")
        cal_comida = 0.0
        prot_comida = 0.0
        
        while True:
            opcion = input("¿Desea agregar un alimento a esta comida? (s/n): ").lower().strip()
            if opcion == 'n':
                break
            elif opcion == 's':
                alimento = input("Nombre del alimento (ej. avena, pechuga de pollo): ").lower().strip()
                
                if alimento not in TABLA_NUTRICIONAL:
                    print("❌ Alimento no registrado en la base de datos. Intente de nuevo.")
                    continue
                
                try:
                    gramos = float(input(f"¿Cuántos gramos consumió de '{alimento}'?: "))
                    if gramos <= 0:
                        print("❌ La cantidad en gramos debe ser mayor a cero.")
                        continue
                except ValueError:
                    print("❌ Entrada inválida. Ingrese un valor numérico.")
                    continue
                
                # Realizar cálculo mediante regla de 3
                cal, prot = calcular_nutrientes(alimento, gramos)
                cal_comida += cal
                prot_comida += prot
                print(f"✔️ Registrado de forma exitosa: {gramos}g de {alimento.capitalize()} -> (+{cal:.2f} kcal, +{prot:.2f}g prote)")
            else:
                print("❌ Entrada no válida. Por favor, marque 's' para Sí o 'n' para No.")
        
        # Mostrar subtotal por cada etapa del día e ir acumulando
        print(f"\n📊 RESUMEN PARCIAL ({comida}): {cal_comida:.2f} kcal | {prot_comida:.2f}g proteína.")
        total_diario_cal += cal_comida
        total_diario_prot += prot_comida

    # Reporte consolidado al final de la jornada laboral/entrenamiento
    print("\n====================================================")
    print("         RESUMEN NUTRICIONAL TOTAL DEL DÍA          ")
    print("====================================================")
    print(f" 🔥 Energía total consumida : {total_diario_cal:.2f} kcal")
    print(f" 💪 Proteínas totales del día: {total_diario_prot:.2f} g")
    print("====================================================")

if __name__ == "__main__":
    ejecutar_registro_diario()