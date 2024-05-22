
class ClassePessoa:
    def __init__(self, nome, numeroConta, tipoConta): #init_ == this
        self.nome = nome
        self.numeroConta = numeroConta
        self.tipoConta = tipoConta
        self.status = False
        self.saldo = 0.0

    def deposito(self, valor):
        if self.status == False:#verifica se a conta está ativa, se não estiver não realiza o depósito
            print("O depósito não pode ser realizado pois a conta não está ativa")
        elif valor <=0:#verifica se o valor é menor ou igual a zero
            print("Não é possivel deposítar um  valor menor ou igual a 0")
        else:
            self.saldo = self.saldo + valor#saldo = saldo + o valor depósitado
            print(f"Saldo atual: R${self.saldo}")

    def sacar(self, valor):
        if self.status == False:#verifica se a conta está ativa
            print("O saque não pode ser realizado pois a conta não está ativa")
        elif self.saldo < valor:#verifica se o saldo é menor do que o valor
            print("Saldo insuficiente")
        else:
            self.saldo = self.saldo - valor
            print(f"Saldo atual: R${self.saldo}")

    def ativarConta(self):
        if self.status == True:#Se status da conta for igual a True, sua conta já está ativa
            print("Sua conta já está ativa")
        else:
            self.status = True#E se recever True, ativa a conta
            print("Conta ativa com sucesso")

    def desativarConta(self):
        if self.saldo > 0:#verifica se tem algum valor na conta
            print(f"Ainda restam R${self.saldo}")
        elif self.status == False:
            print("Sua conta já está está desativada")
        else:
            self.status = False
            print("Conta desativada com sucesso!")

    def verificarConta(self):
            if self.status == False:
                print("Sua conta já está está desativada, você não pode verificar o saldo")
            else:
                print(f"Saldo atual: R${self.saldo}")