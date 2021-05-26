import sqlite3

conn = sqlite3.connect('clientes.db')

cursor = conn.cursor()

# mostrando as colunas da tabela
cursor.execute('PRAGMA table_info({})'. format('clientes'))

coluna = [tupla[1] for tupla in cursor.fetchall()] #para entender melhor o comando, execute sem o [1]

print('Colunas:', coluna)

# mostrando os nomes das tabelas

cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')

print('Nomes de tabela: ')

for nome_de_tabela in cursor.fetchall():
    print(nome_de_tabela)

# conn.commit() não há a necessidade desse comando pois não haverá alteração nos dados

# obtendo o schema da tabela
cursor.execute("""
SELECT sql FROM sqlite_master WHERE type='table' AND name='clientes'
""")

print('Schema: ')

for schema in cursor.fetchall(): # vai mostrar a linha de comando utilizada para definir a tabela e as colunas 
    print(schema, '\n')

conn.close()
