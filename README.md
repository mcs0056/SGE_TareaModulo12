# SGE_TareaModulo12
# Práctica Evaluable – Automatización de Datos en Odoo con Python

## Descripción del Proyecto
Este proyecto consiste en el desarrollo de un script en Python que realiza un proceso **ETL (Extracción, Transformación y Carga)** para importar un listado de centros educativos desde un archivo CSV a una base de datos PostgreSQL utilizada por Odoo, ejecutándose en contenedores Docker.

El objetivo es automatizar la carga de datos externos en el ERP Odoo utilizando herramientas habituales de administración de sistemas.

---

## Tecnologías Utilizadas
- **Python 3.10+**
- **Pandas**
- **psycopg2-binary**
- **PostgreSQL**
- **Docker Desktop**
- **Odoo**
- **Git / GitHub**

---

## Estructura del Proyecto
Tarea_Modulo12/
├── Capturas
├   ├── consola_python.png
├   └── consultaSQL.png
├── docker-compose.yaml
├── importar.py
├── listado.csv
└── README.md

---

## ⚙️ Requisitos Previos
- Docker Desktop instalado y en ejecución
- Contenedores de **Odoo** y **PostgreSQL** activos
- Python 3.10 o superior instalado
- Acceso a la base de datos PostgreSQL de Odoo

---

## Procedimiento de Ejecución

###  Clonar el repositorio
```bash
git clone https://github.com/tu_usuario/odoo-etl-centros.git
cd odoo-etl-centros
```

### Importar dependencias
```bash
pip install pandas psycopg2-binary
```

### Verificar contenedores Docker
```bash
docker ps
```

### Ejecutar el script
```bash
python importar.py
```

### Verificación de datos
SELECT * FROM import_centros;

---

## Capturas de pantalla
<img width="1365" height="719" alt="consola_python" src="https://github.com/user-attachments/assets/48dc75fe-833a-40a1-a781-fe74de054264" />

<img width="1365" height="601" alt="consultaSQL" src="https://github.com/user-attachments/assets/1779345a-090a-4778-8078-310ffb063d12" />

---

## Funcionalidades implementadas
- Lectura de archivos CSV con codificación latin1
- Conexión robusta a PostgreSQL mediante diccionario de credenciales
- Creación automática de la tabla de destino
- Inserción de datos usando bucles e índices iloc
- Gestión de errores y control de transacciones (commit / rollback)
