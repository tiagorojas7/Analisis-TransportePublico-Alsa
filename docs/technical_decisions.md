# 🔧 Decisiones Técnicas - Arquitectura del Proyecto

## 🏗️ Arquitectura Seleccionada
Raw Data → Power Query → Python ETL → SQL Database → Power BI → Insights


## 🤔 ¿Por Qué Esta Stack?

### Power Query para Limpieza Inicial
- **Ventaja:** Interfaz visual para limpieza rápida
- **Uso:** Estandarización de formatos, manejo inicial de nulos
- **Resultado:** Datos consistentes para procesamiento en Python

### Python para Transformación Compleja
- **Librerías:** Pandas (manipulación), NumPy (cálculos), SQLAlchemy (BD)
- **Ventaja:** Flexibilidad para lógica de negocio compleja
- **Ejemplos:** 
  - Clasificación de conductores por experiencia
  - Cálculo de velocidad promedio por ruta
  - Análisis de sentimiento en comentarios

### MySQL para Almacenamiento
- **Ventaja:** Escalabilidad y rendimiento en consultas
- **Uso:** Unificación de datos para análisis cruzado
- **Beneficio:** Consultas complejas entre múltiples tablas

### Power BI para Visualización
- **Ventaja:** Interactividad y conectividad con múltiples fuentes
- **Uso:** Dashboards ejecutivos con drill-down
- **Resultado:** Toma de decisiones basada en visualizaciones claras

## 🚀 Decisiones Clave de Diseño

### 1. Pipeline Modular
Cada etapa es independiente, permitiendo:
- Actualizar una etapa sin afectar las demás
- Escalar componentes individualmente
- Mantener el código de manera organizada

### 2. Metadatos y Documentación
Todas las transformaciones están documentadas para:
- Auditoría de cambios
- Onboarding de nuevos miembros
- Mantenimiento futuro

### 3. Manejo de Calidad de Datos
- Validación de integridad referencial
- Tratamiento consistente de valores nulos
- Estandarización de formatos y categorías
