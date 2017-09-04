# -*- coding: utf-8 -*-
#Este programa utiliza um banco de dados SQLite3 para manipulação de dados
#Foram utilizados comandos SQL para calcular a média e ordenar os clientes

import sqlite3

#Inicia a conexão com o banco de dados
conexao = sqlite3.connect('loja.db')
cursor = conexao.cursor()

#Seleciona a média atentendo os critérios
cursor.execute("""
    SELECT AVG(vl_total) FROM tb_customer_account
    WHERE vl_total > 560 AND id_customer BETWEEN 1500 AND 2700;
""")

print 'Média: {0:.2f}'.format(cursor.fetchall()[0][0])

#Seleciona os registros que atendem aos critérios em ordem decrescente
cursor.execute("""  
    SELECT * FROM tb_customer_account
    WHERE vl_total > 560 AND id_customer BETWEEN 1500 AND 2700
    ORDER BY vl_total DESC;
""")

for linha in cursor.fetchall():
    print 'ID: {} | CPF: {} | Nome: {} | Ativo: {} | Saldo: {}'.format(
        linha[0], linha[1], linha[2], linha[3], linha[4]
    )

conexao.close()