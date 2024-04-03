from contacorrente import ContaCorrente, CartaoCredito
from agencia import AgenciaComum, AgenciaPremium, AgenciaVirtual

conta_caio = ContaCorrente('Caio Henrique Da Silva Cunha', 8044472339,481, 44333)

cartao_caio = CartaoCredito('Caio', conta_caio)
print(cartao_caio.numero)
print(cartao_caio.validade)
print(cartao_caio.codigo_seguranca)


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

