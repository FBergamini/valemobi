# -*- coding: utf-8 -*-
#Este programa cria um banco de dados SQLite3 para posterior manipulação de dados

import sqlite3
import random

#Quantidade de registros a serem inseridos
qntReg = 10000

#Inicia a conexão com o banco de dados
conexao = sqlite3.connect('loja.db')
cursor = conexao.cursor()

#Caso não exista, cria a tabela tb_customer_account
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_customer_account (
        id_customer INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        cpf_cnpj TEXT NOT NULL,
        nm_customer TEXT NOT NULL,
        is_active INTEGER NOT NULL,
        vl_total REAL NOT NULL
    );
""")

#Inicializa a lista de registros
registros = []

for i in range(qntReg):
    #Gera informações aleatórias para cada registro a ser inserido
    cpf = random.randint(10**(11-1),10**11-1)
    nome = 'Nome {}'.format(i)
    ativo = random.randint(0,1)
    vl_total = '{0:.2f}'.format(random.uniform(0.0,10000.0))

    #Armazena os registros na lista
    registros.append((cpf, nome, ativo, vl_total))

#Insere toda a lista no banco de dados
cursor.executemany("""
    INSERT INTO tb_customer_account (cpf_cnpj, nm_customer, is_active, vl_total)
    VALUES (?, ?, ?, ?)
""", registros)

#Grava as alterações realizadas no banco de dados
conexao.commit()

#Encerra a conexão com o banco de dados
conexao.close()