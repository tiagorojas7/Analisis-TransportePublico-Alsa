import pandas as pd
import os
import numpy as np
import datetime as dt

#Definimos la ruta de acceso a la carpeta
ruta=r"C:\Users\santr\OneDrive\Escritorio\Tiago Facu\Archivos proyecto Transporte Publico"
rutaAcesso= r"C:\Users\santr\Downloads"
os.chdir(ruta)

#Leemos los correspondientes dataset que limpiamos anteriormente en power query
df_buses= pd.read_excel("Buses_clean_1.xlsx")
df_drivers=pd.read_excel("Drivers_clean_2.xlsx")
df_passengers=pd.read_excel("Passengers_clean_4.xlsx")
df_routes=pd.read_excel("Routes_clean_3.xlsx")
df_trips=pd.read_excel("Trips_clean_5.xlsx")

## Revisamos que los datasets se hayan cargado correctamente
print("="*50)
print("DATASET BUSES:")
print(df_buses.head())
print(df_buses.info())

print("="*50)
print("DATASET DRIVERS:")
print(df_drivers.head())
print(df_drivers.info())

print("="*50)
print("DATASET PASSENGERS:")
print(df_passengers.head())
print(df_passengers.info())

print("="*50)
print("DATASET ROUTES:")
print(df_routes.head())
print(df_routes.info())

print("="*50)
print("DATASET TRIPS:")
print(df_trips.head())
print(df_trips.info())

## Visualizamos los tipos de datos de las columnas
print("="*50)
print("TIPOS DE DATOS:")
print("Buses:", df_buses.dtypes)
print("Drivers:", df_drivers.dtypes)
print("Passengers:", df_passengers.dtypes)
print("Routes:", df_routes.dtypes)
print("Trips:", df_trips.dtypes)

#Validacion e integridad de datos
#Comprobar que los datos sean coherentes, completos y consistentes entre las diferentes tablas.
#Es decir, asegurarme de que los registros estén bien relacionados y que no existan errores lógicos.

# 1) Revisamos los valores nulos y duplicados de cada dataset

print("Valores nulos en df_buses:")
print(df_buses.isnull().sum())
print("\nValores nulos en df_drivers:")
print(df_drivers.isnull().sum())
print("\nValores nulos en df_passengers:")
print(df_passengers.isnull().sum())
print("\nValores nulos en df_routes:")
print(df_routes.isnull().sum())
print("\nValores nulos en df_trips:")
print(df_trips.isnull().sum())

print("\n" + "----"*50)

print("\nFilas duplicadas en df_buses:")
print(df_buses.duplicated().sum())
print("\nFilas duplicadas en df_drivers:")
print(df_drivers.duplicated().sum())
print("\nFilas duplicadas en df_passengers:")
print(df_passengers.duplicated().sum())
print("\nFilas duplicadas en df_routes:")
print(df_routes.duplicated().sum())
print("\nFilas duplicadas en df_trips:")
print(df_trips.duplicated().sum())

# Reemplazar los valores nulos en 'last_maintenance-clean' con 'uninformed'
df_buses["last_maintenance-clean"] = df_buses['last_maintenance-clean'].fillna('uninformed')

# Mostrar los valores nulos después de reemplazararlos para verificar
print("Valores nulos en df_buses después de reemplazar:")
print(df_buses.isnull().sum())

# Mostrar las primeras filas para ver el cambio
print("\nPrimeras filas de df_buses después de reemplazar los nulos:")
print(df_buses.head())

## verificamos si todos los driver_id existen en trips
## verificamos si todos los route_id existen en trips 
## verificamos si todos los bus_id existen en trip  

print(df_trips["driver_id"].isin(df_drivers["driver_id"]).all())
print(df_trips["route_id"].isin(df_routes["route_id"]).all())
print(df_trips["bus_id"].isin(df_buses["bus_id"]).all())

## verificamos valores fuera de rango 

## Unimos el data frame bus con el date frame trips en un nuevo dataframe
df_merged_trips_buses = pd.merge(df_trips, df_buses, on='bus_id')

##convertimos la columna capacity en numerico para poder ralizar la comparacion 
df_merged_trips_buses['capacity'] = pd.to_numeric(df_merged_trips_buses['capacity'], errors='coerce')

## Creamos un nuevo dataframe y guardamos la comparacion entre pasajeros y capacidad 
df_trips_exceeding_capacity = df_merged_trips_buses[df_merged_trips_buses["passengers"] > df_merged_trips_buses["capacity"]]

## utilizamos el atributo .shape para que nos muestre el numero de filas con esas coincidencias 
print(f"cantidad de viajes excedidos:{df_trips_exceeding_capacity.shape[0]}")   
## utilizamos el 0 para que nos muestre el numero de filas que coinciden,si no lo psuieramos mostraria el numero de columnas que tiene el data frame tambien.

#Enriquecimiento y creacion de metricas
#mi objetivo es crear columnas adicionales que aporten valor analítico.

## ENRIQUECIMIENTO DEL DATASET BUSES
#1) creamos columna para determinar el mes de la ultima revision

# Convertir la columna original a datetime, manejando errores
df_buses["last_maintenance-clean"] = pd.to_datetime(df_buses["last_maintenance-clean"], errors="coerce")

# Usar .dt.month_name() para obtener el nombre del mes
df_buses["last_maintenance_month"] = df_buses["last_maintenance-clean"].dt.month_name()
df_buses["last_maintenance-clean"]=df_buses["last_maintenance-clean"].dt.strftime("%Y-%m-%d")
# Remplamzamos los valores nulos en la columna previamente creada.
df_buses["last_maintenance_month"]=df_buses["last_maintenance_month"].fillna("uninformed")
#Cambiamos el nombre de la columna para evitar problemas 
df_buses=df_buses.rename(columns={
    "model.1":"model"
})



# 2) Clasificamos la capacidad del bus en low,medium,high 

#Convertimos la columna capacity en numeric 
df_buses["capacity"]=pd.to_numeric(df_buses["capacity"],errors="coerce")
## Utilizamos np.where para evaluar las variables definidas 
Low= 500
medium= 700
high= 900
df_buses["Capacity_Category"]= np.where (df_buses["capacity"]<= Low, "low", np.where(df_buses["capacity"]<= medium ,"medium",np.where(df_buses["capacity"]<=high,"high","Uninformed")))
#Remplazamos los valores nulos en nuestra columna Capacity.
df_buses["capacity"]=df_buses["capacity"].fillna("Uninformed")


#3) Creamos una columna para saber cuantos años tienen de uso (tenemos en cuenta el año actual)
fecha_actual = dt.date.today()
añoActual= fecha_actual.year
df_buses["yers_of_use"]= añoActual - df_buses["Año"]
df_buses.head()

# ENREQUECIMIENTO DEL DATASET DRIVERS 
# 1) Creamos una columna para que califique los conductores por nivel profesional 
junior= 5
mid = 15
df_drivers["Experience_Level"]=np.where(df_drivers["years_experience"]<=junior,"Junior",np.where(df_drivers["years_experience"]<=mid,"Mid","Senior"))

#2) creamos una columna para evaluar si tiene alta experiencia (a partir de 20 años)
df_drivers["is_high_experience"]=np.where(df_drivers["years_experience"]>=20,"Yes","No")

#3) Creamos una columna donde agrupa las regiones en una region Macro 
region_map = {
    'North': 'Interior',
    'Central': 'Interior',
    'East': 'Coastal',
    'West': 'Coastal',
    'South': 'Coastal'
}
df_drivers["Region_macro"]=df_drivers["region"].map(region_map)
print(df_drivers.head())

# ENREQUECIMIENTO DEL DATASET ROUTES  
#1) creamos columna para ver la velocidad promedio por ruta (km/h) 
df_routes["average_speed(k/h)"]=(df_routes["distance_km"]*60)/df_routes["avg_duration_min"]
df_routes["average_speed(k/h)"]=df_routes["average_speed(k/h)"].round(1) #Redondeamos a un decimales

#2) clasificamos las rutas por distancia 
df_routes["Route_type"]=np.where(df_routes["distance_km"]<=100,"Short",np.where(df_routes["distance_km"]<=300,"Medium","Long"))


#3) calculamos una columna para saber los km/m, para indentificar rutas con mas congestiones (cuantos minutos tarda en recorrer un km)
df_routes["min_per_km"]= df_routes["avg_duration_min"]/df_routes["distance_km"]
df_routes["min_per_km"]= df_routes["min_per_km"].round(3) #Redondeamos a tres decimales

#4) Creamos una columna donde agrupa las regiones en una region Macro 
region_map = {
    'North': 'Interior',
    'Central': 'Interior',
    'East': 'Coastal',
    'West': 'Coastal',
    'South': 'Coastal'
}
df_routes["Region_macro"]=df_routes["zone"].map(region_map)

#5) creamos una columna booleana para indetificar las rutas que estan por enncima de la velocidad promedio de todas las rutas 
avg_global_speed=df_routes["average_speed(k/h)"].mean()
df_routes["is_high_speed_route"]=df_routes["average_speed(k/h)"]>avg_global_speed

#6) creamos dos columna, unaa para saber que tan rapida es al ruta (min) y otra su clasificacion 
df_routes["speed_route"]=df_routes["distance_km"]/df_routes["avg_duration_min"]*60
del df_routes["speed_route"]
print(df_routes.head(20))

df_routes= df_routes.rename(columns={
    "average_speed(k/h)":"average_speed_km_h"
})

# ENREQUECIMIENTO DEL DATASET PASSENGERS 
#1) Creamos una columna para saber el % de satisfaccion del cliente (cleanlines + punctuality + service )
df_passengers["cleanliness_score"] = pd.to_numeric(df_passengers["cleanliness_score"],errors="coerce")
df_passengers["punctuality_score"] = pd.to_numeric(df_passengers["punctuality_score"],errors="coerce")
df_passengers["service_score"] = pd.to_numeric(df_passengers["service_score"],errors="coerce")

df_passengers["service_score"]=df_passengers["service_score"].fillna(0)
df_passengers["cleanliness_score"]=df_passengers["cleanliness_score"].fillna(0)
df_passengers["punctuality_score"]=df_passengers["punctuality_score"].fillna(0)

df_passengers["avg_satisfaction"] = (df_passengers["cleanliness_score"] + df_passengers["punctuality_score"] + df_passengers["service_score"])/3
df_passengers["avg_satisfaction"]= df_passengers["avg_satisfaction"].round(1)

print(df_passengers.head())

#2) creamos columna para clasificar el # de satisfaccion del cliente, en high,mdium,low
df_passengers["satisfaction_category"]=np.where(df_passengers["avg_satisfaction"]>=40.0,"High",np.where(df_passengers["avg_satisfaction"]>=20.5,"Medium","Low"))


#3) puntuamos los comenatarios, si son positivos le ponemos 1 en caso contrario un 0 
positive_keywords = ['good', 'great', 'excellent', 'polite', 'clean', 'comfortable', 'smooth']
negative_keywords = ['late', 'crowded', 'slow', 'dirty', 'uncomfortable', 'rude']
neutral_keywords = ['Whit out comment']

condition_positive = df_passengers['comment'].str.contains('|'.join(positive_keywords), case=False, na=False) #utilizamos case para que sea insensible a la mayuscula
condition_negative = df_passengers['comment'].str.contains('|'.join(negative_keywords), case=False, na=False) #utilizamos na para que devuelva flase los valores nulos
condition_neutral = df_passengers['comment'].str.contains('|'.join(neutral_keywords), case=False, na=False)

df_passengers['type_of_comment'] = np.where(condition_positive,'Positive', 
np.where(   condition_negative, 'Negative', 
np.where(  condition_neutral, 'Neutral','Other/Undefined')))
df_passengers.head(30)

# Enrequecimiento del dataset trips 
## 1) creamos columna para saber si el bus llego a tiempo (tolerancia 10 minutos ) o estuvo demorado 
df_trips["delay_category"]= np.where(df_trips["delay_min-clean"] <= 10, "On Time","Delayed") 

#2) creamos una columna para ver la eficiencia de por pasajero 
#covertimos las dos columnas en numericas para realizar las operaciones 
df_trips["revenue_usd"]=pd.to_numeric(df_trips["revenue_usd"],errors="coerce")
df_trips["passengers"]=pd.to_numeric(df_trips["passengers"],errors="coerce")

df_trips["efficiency_per_passenger"]=df_trips["revenue_usd"]/df_trips["passengers"]
df_trips["efficiency_per_passenger"]=df_trips["efficiency_per_passenger"].round(2)
df_trips["efficiency_per_passenger"]=df_trips["efficiency_per_passenger"].fillna(0)
df_trips["revenue_usd"] = df_trips["revenue_usd"].fillna(0)

#3) creamos columna para clasificar en high, medium, low la columna reveneu_usd
df_trips["revenue_category"]=np.where(df_trips["revenue_usd"]>=100000,"High",np.where(df_trips["revenue_usd"]>=25000,"Medium",np.where(df_trips["revenue_usd"]>=1,"low","uninformed")))

df_trips["Date-Clean"]=pd.to_datetime(df_trips["Date-Clean"])
df_trips["Date-Clean"]=df_trips["Date-Clean"].dt.strftime("%Y-%m-%d")
df_trips.head()

#EXPORTAMOS LOS NUEVOS DATAFRAMES EN FORMATO XSLX
print("EXPORTANDO ARCHIVOS EN FORMATO EXCEL...")

df_buses.to_excel("Buses_finished.xlsx", index=False)
df_drivers.to_excel("Drivers_finished.xlsx", index=False)
df_passengers.to_excel("Passengers_finished.xlsx", index=False)
df_routes.to_excel("Routes_finished.xlsx", index=False)
df_trips.to_excel("Trips_finished.xlsx", index=False) 

print(f"ARCHIVOS EXPORTADOS CORRECTAMENTE, los puedes encontrar en {ruta}")

#EXPORTAMOS LOS NUEVOS DATAFRAMES A UNA BASE DE DATOS SQL
from sqlalchemy import create_engine

database = {
    'host': '127.0.0.1',          
    'user': 'root',                
    'password': 'root',     
    'database': 'transportepublico',
    'port': 3306                   
}

connection_string = f"mysql+mysqlconnector://{database['user']}:{database['password']}@{database['host']}:{database['port']}/{database['database']}"
con=create_engine(connection_string)

print("EXPORTANDO ARCHIVOS A TU BASE DE DATOS SQL...")

df_buses.to_sql('buses', con=connection_string, if_exists='replace', index=False)
df_drivers.to_sql('drivers', con=connection_string, if_exists='replace', index=False)
df_passengers.to_sql('passengers', con=connection_string, if_exists='replace', index=False)
df_routes.to_sql('routes', con=connection_string, if_exists='replace', index=False)
df_trips.to_sql('trips', con=connection_string, if_exists='replace', index=False)

print("Archivos exportados correctamente a tu base de datos Sql")

