from random import randint

class Agencia:
    def __init__(self, telefone, CNPJ, numero):
        self.telefone = telefone
        self.CNPJ = CNPJ
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []


    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'Caixa abaixo do nível recomendado: {self.caixa}')

        else:
            print(f'O valor de caixa está ok. Caixa Atual: {self.caixa}')


    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa> valor:
            self.emprestimos.append((valor, cpf, juros))
        else: 
            print('Emprestivo não foi possivel, não temos caixa')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):
    def __init__(self, site, telefone, CNPJ):#inicializando a subclasse 
        self.site = site
        super().__init__(telefone, CNPJ, 1000) #chamando o init da classe mae, para que não seja necessario informar os mesmo atributos ja herdados.
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal +=valor

    def sacar_paypal(self,valor):
        self.caixa_paypal -= valor
        self.caixa +=valor

class AgenciaComum(Agencia):
    
    def __init__(self, telefone, CNPJ):
        super().__init__(telefone, CNPJ, numero=randint(1001,9999))
        self.caixa = 1000000

class AgenciaPremium(Agencia):
    def __init__(self, telefone, CNPJ):
        super().__init__(telefone, CNPJ, numero=randint(1001,9999))
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            #adicionando cliente   
            super().adicionar_cliente(nome, cpf, patrimonio)    
        else:
            print("O cliente não tem patrimonio mínimo")







agencia1 = AgenciaVirtual("www.caio.com.br", 23445, 4480)
agencia1.caixa = 100000000
#agencia1.verificar_caixa()
agencia1.adicionar_cliente('Caio', 80, 2000)


agencia1.depositar_paypal(200000)
print(agencia1.caixa)
print(agencia1.caixa_paypal)


agencia_premium = AgenciaPremium(333333, 10000)
agencia_premium.adicionar_cliente('caio', 234449, 200)
print(agencia_premium.clientes)
