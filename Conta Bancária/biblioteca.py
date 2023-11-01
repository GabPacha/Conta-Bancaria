class ContaBancaria:
    def __init__(self, nome, numero, tipo):
        self.nome = nome
        self.numero = numero
        self.tipo = tipo
        self.saldo = 0
        self.status = False
        self.limite = 0


    def verificarsaldo(self):
        print(f"O seu saldo atual é de {self.saldo} reais")


    def ativarconta(self):
        if self.status == False:
            self.status = True
            print("Conta ativada com sucesso.")

        else:
            print("Conta ja estava ativada.")


    def desativarconta(self):
        if self.saldo == 0:
            if self.status == True:
                self.status == False
                print("Conta desativada com sucesso.")
        elif self.saldo<0:
            print("Sua conta não pode ser desativada,você está em divida.")

        else:
            print("Sua conta não pode ser desativada, você deve esvazia-la para que seja possivel.")

    def ativarlimite(self):
        print("Parabens, foi aprovado para você um limite de 500 reais para a sua conta.")
        self.limite=500



    def depositar(self, deposito):
        if self.status == True:
            self.saldo = self.saldo + deposito
            print(f"Deposito efetuado com sucesso, seu saldo agora é {self.saldo} reais")
        else:
            print("Conta inativa.")


    def sacar(self, saque):
        if self.status == True:

            if saque > self.saldo+self.limite:
                print(f"Não foi possivel finalizar a operação.O limite de credito de {self.limite} foi atingido.")

            else:
                self.saldo = self.saldo - saque
                print(f"Você sacou {saque} reais, seu saldo agora é de {self.saldo} reais")

        else:
            print("Conta inativa.")