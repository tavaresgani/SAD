import sqlite3 as s

# Criar objeto de conexão e conectar ao banco
conn = s.connect('banco_rh.db')

# Criar cursor
cur = conn.cursor()

# Determinar declarações SQL a serem executadas e executá-las no banco

#Cria a tabela CARGO
cur.execute("CREATE TABLE cargo(cargoId int not null, cargoNm varchar(80), min_Sal NUMERIC(10,2), max_Sal NUMERIC(10,2), PRIMARY KEY (cargoId));").fetchall()

#Cria a tabela FUNCIONARIO
cur.execute("CREATE TABLE funcionario(funcId INT NOT NULL, cargoId INT NOT NULL, funcNm varchar(80), sal NUMERIC(10,2), PRIMARY KEY(funcId, cargoId), FOREIGN KEY (cargoId) REFERENCES cargo(cargoId));").fetchall()
conn.commit()

#Insere os dados na tabela CARGO
cur.execute("INSERT INTO cargo VALUES(1, 'Gerente', 1000, 3000);")
cur.execute("INSERT INTO cargo VALUES(2, 'Secretaria', 500, 800);")
cur.execute("INSERT INTO cargo VALUES(3, 'Office Boy', 300, 490);")
conn.commit()

#Insere os dados na tabela FUNCIONARIO
cur.execute("INSERT INTO funcionario VALUES(1, 1, 'Carlos', 2750);")
cur.execute("INSERT INTO funcionario VALUES(1, 2, 'Maria', 825);")
cur.execute("INSERT INTO funcionario VALUES(1, 3, 'Joao', 420);")
cur.execute("INSERT INTO funcionario VALUES(2, 3, 'Miguel', 500);")
conn.commit()

res = cur.execute("SELECT f.funcNm, c.cargoNm, f.sal, c.max_Sal FROM funcionario as f INNER JOIN cargo as c ON (c.cargoId = f.cargoId) WHERE (f.sal > c.max_Sal);").fetchall()



# Verificar se tabelas foram criadas
print(res)

cur.close()
conn.close()

