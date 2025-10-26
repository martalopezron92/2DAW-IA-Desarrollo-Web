#!/usr/bin/env python3
"""
Script de validación de datasets para el curso de IA aplicada al Desarrollo Web
Verifica que todos los archivos CSV tienen la estructura adecuada para las prácticas
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys

def validar_dataset(archivo, descripcion, validaciones):
    """Valida un dataset específico"""
    print(f"\n🔍 Validando {descripcion}")
    print("-" * 50)
    
    try:
        # Cargar el dataset
        df = pd.read_csv(archivo)
        print(f"✅ Archivo cargado correctamente: {len(df)} filas")
        
        # Mostrar información básica
        print(f"📊 Columnas ({len(df.columns)}): {', '.join(df.columns)}")
        print(f"📏 Dimensiones: {df.shape}")
        
        # Ejecutar validaciones específicas
        errores = []
        for validacion in validaciones:
            try:
                resultado = validacion(df)
                if resultado is True:
                    continue
                elif resultado is False:
                    errores.append("Validación falló")
                else:
                    errores.append(resultado)
            except Exception as e:
                errores.append(f"Error en validación: {str(e)}")
        
        if errores:
            print("❌ Errores encontrados:")
            for error in errores:
                print(f"   - {error}")
            return False
        else:
            print("✅ Todas las validaciones pasaron correctamente")
            return True
            
    except Exception as e:
        print(f"❌ Error al cargar el archivo: {str(e)}")
        return False

def validar_clientes_clustering(df):
    """Validaciones específicas para clustering de clientes"""
    # Verificar columnas requeridas
    columnas_requeridas = ['cliente_id', 'edad', 'gasto_total']
    for col in columnas_requeridas:
        if col not in df.columns:
            return f"Falta columna requerida: {col}"
    
    # Verificar tipos de datos
    if not pd.api.types.is_numeric_dtype(df['edad']):
        return "La columna 'edad' debe ser numérica"
    
    if not pd.api.types.is_numeric_dtype(df['gasto_total']):
        return "La columna 'gasto_total' debe ser numérica"
    
    # Verificar rangos razonables
    if df['edad'].min() < 18 or df['edad'].max() > 100:
        return "Edades fuera del rango esperado (18-100)"
    
    if df['gasto_total'].min() < 0:
        return "Gastos negativos encontrados"
    
    return True

def validar_precios_regresion(df):
    """Validaciones específicas para regresión de precios"""
    # Verificar columnas requeridas
    columnas_requeridas = ['metros_cuadrados', 'habitaciones', 'precio']
    for col in columnas_requeridas:
        if col not in df.columns:
            return f"Falta columna requerida: {col}"
    
    # Verificar tipos de datos numéricos
    for col in ['metros_cuadrados', 'habitaciones', 'banos', 'antiguedad', 'precio']:
        if col in df.columns and not pd.api.types.is_numeric_dtype(df[col]):
            return f"La columna '{col}' debe ser numérica"
    
    # Verificar variables binarias
    for col in ['parking', 'ascensor', 'terraza']:
        if col in df.columns:
            valores_unicos = df[col].unique()
            if not all(v in [0, 1] for v in valores_unicos):
                return f"La columna '{col}' debe ser binaria (0/1)"
    
    # Verificar rangos razonables
    if df['metros_cuadrados'].min() < 20 or df['metros_cuadrados'].max() > 500:
        return "Metros cuadrados fuera del rango esperado (20-500)"
    
    if df['precio'].min() < 50000 or df['precio'].max() > 2000000:
        return "Precios fuera del rango esperado (50k-2M)"
    
    return True

def validar_resenas_sentimientos(df):
    """Validaciones específicas para análisis de sentimientos"""
    # Verificar columnas requeridas
    columnas_requeridas = ['texto', 'sentimiento', 'puntuacion']
    for col in columnas_requeridas:
        if col not in df.columns:
            return f"Falta columna requerida: {col}"
    
    # Verificar sentimientos válidos
    sentimientos_validos = ['positivo', 'negativo', 'neutro']
    sentimientos_encontrados = df['sentimiento'].unique()
    for sent in sentimientos_encontrados:
        if sent not in sentimientos_validos:
            return f"Sentimiento inválido encontrado: {sent}"
    
    # Verificar puntuaciones
    if not pd.api.types.is_numeric_dtype(df['puntuacion']):
        return "La columna 'puntuacion' debe ser numérica"
    
    if df['puntuacion'].min() < 1 or df['puntuacion'].max() > 5:
        return "Puntuaciones fuera del rango esperado (1-5)"
    
    # Verificar que hay texto en todas las reseñas
    if df['texto'].isnull().any():
        return "Hay reseñas sin texto"
    
    # Verificar longitud mínima de texto
    if df['texto'].str.len().min() < 10:
        return "Algunas reseñas son demasiado cortas"
    
    return True

def validar_ventas_siuba(df):
    """Validaciones específicas para práctica de Siuba"""
    # Verificar columnas requeridas
    columnas_requeridas = ['cliente_id', 'fecha', 'categoria', 'cantidad', 'precio_unitario']
    for col in columnas_requeridas:
        if col not in df.columns:
            return f"Falta columna requerida: {col}"
    
    # Verificar tipos de datos
    if not pd.api.types.is_numeric_dtype(df['cantidad']):
        return "La columna 'cantidad' debe ser numérica"
    
    if not pd.api.types.is_numeric_dtype(df['precio_unitario']):
        return "La columna 'precio_unitario' debe ser numérica"
    
    # Verificar fechas
    try:
        pd.to_datetime(df['fecha'])
    except:
        return "La columna 'fecha' tiene formato inválido"
    
    # Verificar valores positivos
    if df['cantidad'].min() <= 0:
        return "Las cantidades deben ser positivas"
    
    if df['precio_unitario'].min() <= 0:
        return "Los precios unitarios deben ser positivos"
    
    return True

def mostrar_estadisticas_basicas(archivo, nombre):
    """Muestra estadísticas básicas del dataset"""
    df = pd.read_csv(archivo)
    print(f"\n📈 Estadísticas básicas - {nombre}")
    print("-" * 30)
    
    # Columnas numéricas
    cols_numericas = df.select_dtypes(include=[np.number]).columns
    if len(cols_numericas) > 0:
        print("Variables numéricas:")
        for col in cols_numericas:
            print(f"  {col}: min={df[col].min():.1f}, max={df[col].max():.1f}, media={df[col].mean():.1f}")
    
    # Columnas categóricas
    cols_categoricas = df.select_dtypes(include=['object']).columns
    if len(cols_categoricas) > 0:
        print("\nVariables categóricas:")
        for col in cols_categoricas:
            valores_unicos = len(df[col].unique())
            print(f"  {col}: {valores_unicos} valores únicos")

def main():
    """Función principal de validación"""
    print("🚀 VALIDACIÓN DE DATASETS PARA PRÁCTICAS DE IA")
    print("=" * 60)
    
    base_path = Path("materiales/datos")
    
    # Definir archivos y sus validaciones
    validaciones = [
        {
            'archivo': base_path / "clientes_tienda.csv",
            'descripcion': "Clientes (P06 - Clustering)",
            'validaciones': [validar_clientes_clustering]
        },
        {
            'archivo': base_path / "precios_vivienda.csv", 
            'descripcion': "Precios vivienda (P05 - Regresión)",
            'validaciones': [validar_precios_regresion]
        },
        {
            'archivo': base_path / "reseñas_sentimientos.csv",
            'descripcion': "Reseñas sentimientos (Deep Learning - NLP)",
            'validaciones': [validar_resenas_sentimientos]
        },
        {
            'archivo': base_path / "ventas_siuba.csv",
            'descripcion': "Ventas (P04b - Siuba)",
            'validaciones': [validar_ventas_siuba]
        }
    ]
    
    # Ejecutar validaciones
    resultados = []
    for validacion in validaciones:
        archivo = validacion['archivo']
        if not archivo.exists():
            print(f"\n❌ Archivo no encontrado: {archivo}")
            resultados.append(False)
            continue
            
        resultado = validar_dataset(
            archivo,
            validacion['descripcion'], 
            validacion['validaciones']
        )
        resultados.append(resultado)
        
        # Mostrar estadísticas si la validación pasó
        if resultado:
            mostrar_estadisticas_basicas(archivo, validacion['descripcion'])
    
    # Resumen final
    print("\n" + "=" * 60)
    print("📋 RESUMEN DE VALIDACIÓN")
    print("=" * 60)
    
    exitosos = sum(resultados)
    total = len(resultados)
    
    if exitosos == total:
        print(f"🎉 ¡ÉXITO! Todos los datasets ({exitosos}/{total}) están listos para las prácticas")
        print("\n✅ Los estudiantes pueden comenzar con:")
        print("   • P04b: Análisis con Siuba")
        print("   • P05: Regresión lineal con precios de vivienda")
        print("   • P06: Clustering de clientes") 
        print("   • Deep Learning: Análisis de sentimientos")
    else:
        print(f"⚠️  {exitosos}/{total} datasets validados correctamente")
        print("❌ Revisa los errores anteriores antes de comenzar las prácticas")
        sys.exit(1)

if __name__ == "__main__":
    main()