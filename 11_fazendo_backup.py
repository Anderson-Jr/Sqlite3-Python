import sqlite3
import io  

#salva os dados num arquivo externo através do método write

conn = sqlite3.connect('clientes.db')

cursor = conn.cursor()

with io.open('clientes_dump.sql', 'w') as f:
    for linha in conn.iterdump():
        f.write('{%s\n}' % linha)

print('Backup realizado com sucesso.')

print('salvo como clientes_dump.sql')

# conn.commit() apenas fazendo backup, nenhum dado do banco será alterado

conn.close()