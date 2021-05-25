import sqlite3

conn = sqlite3.connect('clientes.db')

cursor = conn.cursor()

#deletando dados 
 
id_cliente = 8

cursor.execute("""
DELETE FROM clientes 
WHERE id = ?
""", (id_cliente,))

conn.commit()

print('Registro excluído com sucesso.')

conn.close()