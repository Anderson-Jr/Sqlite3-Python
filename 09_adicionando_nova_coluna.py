import sqlite3 

conn = sqlite3.connect('clientes.db')

cursor = conn.cursor()

# adicionando nova coluna

cursor.execute("""
ALTER TABLE clientes 
ADD COLUMN bloqueado BOOLEAN
""")

conn.commit()

print('Novo campo foi adicionado com sucesso.')

conn.close()