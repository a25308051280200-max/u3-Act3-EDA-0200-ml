import pandas as pd
import matplotlib.pyplot as plt

# 1. Crear diccionario con datos de empleados
empleados = {
    'id_empleado': [101, 102, 103, 104, 105, 106],
    'nombre': ['Carlos', 'Maria', 'Jose', 'Ana', 'Luis', 'Sofia'],
    'edad': [25, 32, 28, 40, 35, 29],
    'departamento': ['Produccion', 'Calidad', 'Mantenimiento', 'Produccion', 'Calidad', 'Mantenimiento'],
    'puesto': ['Operador', 'Inspector', 'Tecnico', 'Supervisor', 'Inspector', 'Tecnico'],
    'salario': [12000, 15000, 13500, 22000, 16000, 14500],
    'antiguedad': [2, 6, 4, 12, 8, 3],
    'horas_trabajadas': [48, 40, 45, 40, 42, 48],
    'capacitaciones': [2, 5, 3, 8, 6, 4],
    'desempeno': [80, 95, 85, 98, 90, 88]
}

print("Analisis Exploratorio de Datos EDA ")
print("EDA, Explorar Datalysis por Alejandra Rivera Valenzuela NC = 0200")
print("5. Crear el diccionario con 10 listas y 6 elementos")
# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(empleados)
print("\n--- TABLA ORIGINAL DE EMPLEADOS ---")
print(df)
print("\nDICCIONARIO ML")

# 3. Exportar los datos a CSV
print("<3<3<3<3<3 Convertir el DataFrame en archivo CSV <3<3<3<3<3")
df.to_csv(
    'empleados_industria_0200.csv',
    index=False,
    encoding='utf-8-sig'
)
print("\n✅ Archivo CSV creado correctamente")
print("<3<3<3<3 8. Leer los datos desde el archivo CSV<3<3<3<3  ")
print("empleados_industria_0200.csv")
# 4. Leer el archivo CSV
df = pd.read_csv('empleados_industria_0200.csv')
print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)
print("<3<3<3<3 9. Análisis Exploratorio de Datos (EDA) <3<3<3<3")
# 5. Primeros y últimos registros
print("<3<3<3<3 \n1. PRIMEROS REGISTROS (Head):<3<3<3<3")
print(df.head(3)) # Muestra los primeros 3
print("<3<3<3<3 \n2. ÚLTIMOS REGISTROS (Tail): <3<3<3<3")
print(df.tail(2)) # Muestra los últimos 2

# 6. Dimensiones y estructura
print("# <3<3<3<3 6. Dimensiones y estructura <3<3<3<3")
print(df) # mostrar matriz
print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)
print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)
print("\n5. TIPOS DE DATOS:\n", df.dtypes)
print("\n6. INFORMACIÓN GENERAL:")
df.info()
# 7. Estadísticas y limpieza
print("<3<3<3<3\n7. ESTADÍSTICAS DESCRIPTIVAS:<3<3<3<3")
print(df.describe())

print("<3<3<3<3\n8. VALORES FALTANTES (Nulls):<3<3<3<3")
print(df.isnull().sum())

print("<3<3<3<3 \n9. REGISTROS DUPLICADOS: <3<3<3<3")
print(df.duplicated().sum())

print("<3<3<3<3 \n10. VALORES ÚNICOS POR COLUMNA: <3<3<3<3")
print(df.nunique())
print("Departamentos únicos:", df['departamento'].unique())
# 8. Análisis específico
print(df)
print("------------------------------------------------------------------")
print("\n11. EMPLEADOS POR DEPARTAMENTO:")
print(df['departamento'].value_counts())

print("\n12. PROMEDIO DE SALARIO: $", df['salario'].mean())
print("13. SALARIO MÁXIMO: $", df['salario'].max())
print("14. SALARIO MÍNIMO: $", df['salario'].min())

# 9. Ordenamiento, filtrado y agrupación
print("<3<3<3<3 \n15. EMPLEADOS ORDENADOS POR SALARIO (Mayor a menor): <3<3<3<3")
print(df.sort_values(by='salario', ascending=False))

print("<3<3<3<3 \n16. EMPLEADOS CON SALARIO MAYOR A $15,000: <3<3<3<3")
filtro = df[df['salario'] > 15000]
print(filtro)

print("\n17. RESUMEN POR DEPARTAMENTO:")
resumen = df.groupby('departamento').agg(
    empleados=('id_empleado', 'count'),
    salario_promedio=('salario', 'mean'),
    salario_maximo=('salario', 'max')
)
print(resumen)

# 18. Gráfica de barras: Empleados por departamento
print("Gráfica de barras: Empleados por departamento")
conteo = df['departamento'].value_counts()

plt.figure(figsize=(8, 5))
barras = plt.bar(conteo.index, conteo.values, color='skyblue')

# Agrega el valor de Y encima de cada barra
plt.bar_label(barras, padding=3)

plt.title('Empleados por departamento Alejandra 0200')
plt.xlabel('Departamento')
plt.ylabel('Cantidad de empleados')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
# 19. Gráfica de barras: Salarios por empleado
plt.figure(figsize=(8, 5))
plt.bar(df['nombre'], df['salario'], color='lightgreen')
plt.title('Salario mensual por empleado EDA por Alejandra 0200')
plt.xlabel('Empleado')
plt.ylabel('Salario en pesos')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
# 20. Histograma: Distribución de edades
plt.figure(figsize=(8, 5))
plt.hist(df['edad'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de edades de empleados EDA por Alejandra 0200')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
# 21. Gráfica de dispersión: Edad vs Salario
plt.figure(figsize=(8, 5))
plt.scatter(df['edad'], df['salario'], color='red', s=100)
plt.title('Relación entre edad y salario EDA por Alejandra 0200')
plt.xlabel('Edad')
plt.ylabel('Salario mensual')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
# 22. Diagrama de caja: Distribución de salarios
plt.figure(figsize=(7, 5))
plt.boxplot(df['salario'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Distribución de salarios (Boxplot) EDA Alejandra 0200')
plt.ylabel('Salario mensual')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
# 23. Matriz de correlación
correlacion = df.corr(numeric_only=True)
print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title('Matriz de correlación de variables numéricas EDA Alejandra 0200')
plt.tight_layout()
plt.show()