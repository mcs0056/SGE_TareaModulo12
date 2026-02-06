import pandas as pd
import psycopg2

# Parámetros de conexión a PostgreSQL
params = {
    "host": "localhost",
    "port": 5432,
    "dbname": "postgres",
    "user": "odoo",
    "password": "odoo"
}

# Ruta del archivo CSV
ruta_csv = r"C:/Users/Usuario1/Desktop/Tarea_Modulo12/listado.csv"

try:
    # Leer el archivo CSV
    df = pd.read_csv(ruta_csv, encoding="latin1")
    print("Archivo listado.csv leído correctamente")

    # Conexión a PostgreSQL
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    print("Conexión con PostgreSQL establecida.")

    # Crear tabla si no existe
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contactos_mailing (
            id SERIAL PRIMARY KEY,
            nombre TEXT,
            domicilio TEXT,
            localidad TEXT,
            cp TEXT,
            telefono TEXT
        );
    """)

    # Insertar datos del CSV en la tabla
    for _, row in df.iterrows():
        cur.execute(
            """
            INSERT INTO contactos_mailing (
                nombre, domicilio, localidad, cp, telefono
            ) VALUES (%s, %s, %s, %s, %s)
            """,
            (
                str(row.iloc[0]),  # Nombre
                str(row.iloc[1]),  # Domicilio
                str(row.iloc[2]),  # Localidad
                str(row.iloc[3]),  # Código postal
                str(row.iloc[4])   # Teléfono
            )
        )

    # Confirmar cambios
    conn.commit()
    print(f"¡Éxito! Se han importado {len(df)} contactos.")

except Exception as e:
    print(f"Ha ocurrido un error: {e}")
    if "conn" in locals():
        conn.rollback()

finally:
    # Cerrar recursos
    if "cur" in locals():
        cur.close()
    if "conn" in locals():
        conn.close()
