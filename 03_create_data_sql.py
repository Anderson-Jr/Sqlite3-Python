import sqlite3

conn = sqlite3.connect('clientes.db')

cursor = conn.cursor()

#inserindo dados na tabela
cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Regis', 35, '000000000000', 'regis@gmail.com', '11-98765-4321', 'Sao Paulo', 'SP', '2014-06-09')
""")

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Aloisio', 87, '11111111111', 'aloisio@email.com', '11-98765-3422', 'Sao Paulo', 'SP', '2014-06-09')
""")

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em) 
VALUES ('Bruna', 21, '22222222222', 'bruna@emai.com', '21-987654-323', 'Campinas', 'SP', '2014-06-08')
""")

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Matheus', 19, '33333333333', 'matheus@email.com', '11-98765-4324', 'Campinas', 'SP', '2014-06-08')
""")

#gravando no BD
conn.commit()

print('Dados inseridos com sucesso')

conn.close()