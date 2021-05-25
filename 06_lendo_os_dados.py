import sqlite3

conn = sqlite3.connect('clientes.db')

cursor = conn.cursor()

# lendo os dados

cursor.execute("""
SELECT * FROM clientes
""")

for linha in cursor.fetchall(): #serve para mostrar cada linha da função SELECT do sqlite3 no terminal python
    print(linha)

conn.close()