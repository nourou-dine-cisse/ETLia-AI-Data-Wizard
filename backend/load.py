import pyodbc

from config import UID, PWD  # tes identifiants

# Connexion SQL Server
DRIVER = '/opt/homebrew/lib/libmsodbcsql.18.dylib'
SERVER = 'localhost,1433'  # ou host.docker.internal si Docker
DATABASE = 'master'

conn_str = (
    f"DRIVER={DRIVER};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"UID={UID};"
    f"PWD={PWD};"
    "Encrypt=no;"
    "TrustServerCertificate=yes;"
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Récupérer toutes les tables du schéma dbo
cursor.execute("""
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE='BASE TABLE' AND TABLE_SCHEMA='dbo'
""")
tables = [row[0] for row in cursor.fetchall()]

# Récupérer toutes les colonnes pour chaque table
schema = {}
for table in tables:
    cursor.execute(f"""
    SELECT COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME='{table}' AND TABLE_SCHEMA='dbo'
    """)
    cols = [row[0] for row in cursor.fetchall()]
    schema[table] = cols

cursor.close()
conn.close()

print(schema)
