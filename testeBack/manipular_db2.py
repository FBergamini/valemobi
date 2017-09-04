# -*- coding: utf-8 -*-
#Este programa utiliza um banco de dados SQLite3 para manipulação de dados
#Foi utilizado comando SQL apenas para obter os dados da tabela e, em seguida, os manipular

import sqlite3
import operator

class Cliente():
    def __init__(self, id, cpf, nome, ativo, saldo):
        self.id = id
        self.cpf = cpf
        self.nome = nome
        self.ativo = ativo
        self.saldo = saldo

#Inicia a conexão com o banco de dados
conexao = sqlite3.connect('loja.db')
cursor = conexao.cursor()

#Seleciona todos os registros da tabela tb_customer_account
cursor.execute("""
    SELECT * FROM tb_customer_account;
""")

soma = 0
contador = 0
clientes = []

#Adiciona os clientes que atendem aos critérios à lista clientes
#Soma os valores do saldo na variável soma
#cursor.fetchall() possui todos os registros retornados do comando SQL
for linha in cursor.fetchall():
    if linha[0] >= 1500 and linha[0] <= 2700 and linha[4] > 560:
        soma += linha[4]
        contador += 1
        clientes.append(Cliente(linha[0], linha[1], linha[2], linha[3], linha[4]))

#Ordena a lista por ordem reversa (decrescente) de saldo
clientes.sort(key=operator.attrgetter('saldo'), reverse=True)

#Calcula e exibe a média dos saldos
print 'Média: {0:.2f}'.format(soma/contador)

for cliente in clientes:
    print 'ID: {} | CPF: {} | Nome: {} | Ativo: {} | Saldo: {}'.format(
            cliente.id, cliente.cpf, cliente.nome, cliente.ativo, cliente.saldo
        )
    
#Encerra a conexão com o banco de dados
conexao.close()
