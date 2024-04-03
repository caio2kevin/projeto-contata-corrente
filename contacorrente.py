from datetime import datetime
import pytz
from random import randint

class ContaCorrente:

    """
    cria um objeto ContaCorrente para gerenciar as contas do clientes

    atributos
    nome = nome do cliente
    cpf = cpf do cliente
    agencia = numero da agencia do cliente
    num_conta = numero da conta do cliente
    limite = mostra o limite do cliente
    transacoes = mostra as transacoes feitas na conta do cliente.  

    """

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')#ajuste de horas 

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        print(f'Ola, {self.nome} seu saldo atual é R${self.saldo}')

    def depositar(self, valor):
        self.saldo = valor
        print(f'Voce depositou R${valor}')
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))#para usar o metodo estatico usa-se a classe e o metodo.
        
    def limite_conta(self):
        self.limite = -1000
        return self.limite
    
    def sacar_dinheiro(self, valor):
        if self.saldo - valor <self.limite_conta():
            print('Você não tem saldo suficiente')

        else:
            self.saldo-=valor
            print(f'Você sacou R${valor}')
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))

    def consultar_limite_chequeespecial(self):
        print(f'Seu limite é de {self.limite_conta()}')


    def historico_de_transacoes(self):
        print('Historico de transações: ')
        for transacao in self.transacoes:
            print(transacao)


    def transferir(self, valor, conta_destino):
        self.saldo-=valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora())) 


class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR
    
    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = f'{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 4}'
        self.codigo_seguranca = f'{randint(0,9)}{randint(0,9)}{randint(0,9)}'
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

