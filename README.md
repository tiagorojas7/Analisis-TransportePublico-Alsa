
# 🚀 Análisis de Eficiencia Operativa - ALSA | Pipeline de Datos Completo Automatizado

## 📊 Resumen Ejecutivo

Solución integral de análisis de datos que transforma información operativa cruda en **inteligencia de negocio accionable** para optimización del transporte público. Este pipeline automatizado procesa 100+ buses, 3000+ viajes y feedback de pasajeros para impulsar decisiones basadas en datos.

**✨ Lo que logré:**
- **Automaticé** el procesamiento de 100+ buses y 3000+ viajes
- **Identifiqué** 43.2% de oportunidades de reducción de retrasos  
- **Creé** dashboards ejecutivos para monitoreo en tiempo real
- **Ahorré** 20+ horas mensuales en reportes manuales

## 🛠️ Arquitectura del Proyecto

### Flujo de Datos End-to-End
 Datos Crudos →  Power Query →  Python → SQL →  Power BI →  Insights

### Tecnologías Utilizadas
| Etapa | Herramientas |
|-------|-------------|
| **Limpieza** | Power Query |
| **Procesamiento** | Python (Pandas, NumPy) |
| **Base de Datos** | MySQL |
| **Visualización** | Power BI |
| **Automatización** | Scripts Python |

**📁 Estructura del Proyecto**

├── 📊 DATOS/                       
- [01.originales](https://github.com/tiagorojas7/Analisis-TransportePublico-Alsa/tree/main/datos/01_originales)  -Datos Crudos      
- [02.procesados](https://github.com/tiagorojas7/Analisis-TransportePublico-Alsa/tree/main/datos/02_procesados)  -Datos limpios ( Power query )
- [03.final](https://github.com/tiagorojas7/Analisis-TransportePublico-Alsa/tree/main/datos/03_final)  - Dataframes Enriquecidos para su respectivo analisis ( Python ) 

├── 🔧 CODIGO/                         
- [Script Python TransportePublico](https://github.com/tiagorojas7/Analisis-TransportePublico-Alsa/blob/main/codigo/Script%20Python%20TransportePublico.py) - Script Python 
- [consulta general SQL.sql](https://github.com/tiagorojas7/Analisis-TransportePublico-Alsa/blob/main/codigo/consulta%20general%20SQL.sql) - Consulta general SQL       

├── 📈 DASHBOARDS/                     
- [01_dashboard_PerformanceGeneral.png](https://github.com/tiagorojas7/Analisis-TransportePublico-Alsa/blob/main/dashboards/01-Dashboard_PerformanceGeneral.png)  - Estadisiticas Generales 
- [02_dashboard_eficiencia.png](https://github.com/tiagorojas7/Analisis-TransportePublico-Alsa/blob/main/dashboards/02-Dashboard_EficienciaOperacional.png) - Eficiencia Operacional 
- [03_dashboard_rentabilidad.png](https://github.com/tiagorojas7/Analisis-TransportePublico-Alsa/blob/main/dashboards/03-Dashboard_RentabilidadOperativa.png)  - Rentabilidad Operativa
- [Dashboard Completo](https://github.com/tiagorojas7/Analisis-TransportePublico-Alsa/blob/main/dashboards/Dashboard_Transportepublico.pbix) - Documento para descargar 

 ├──📋 documentacion/                 
 - [contexto_negocio.md](https://github.com/tiagorojas7/Analisis-TransportePublico-Alsa/blob/main/documentacion/contexto_negocio.md)  -Contexto y Problemas a resolver      
 - [decisiones_tecnicas.md]()     


**🔍 ¿Qué Encontrarás Aquí?**
✅ Pipeline ETL completo desde datos crudos hasta dashboards

✅ Análisis de negocio real con impacto cuantificable

✅ Código profesional listo para producción

✅ Documentación clara para replicar el proyecto


**📞 Para Reclutadores**
Si estás evaluando mi perfil para una posición de Analista de Datos, te invito a revisar:
🎯 para_reclutadores/              # Sección especial hiring
    ├── puntos_destacados.md           # Por qué este proyecto destaca
    └── habilidades_demostradas.md     # Competencias técnicas





