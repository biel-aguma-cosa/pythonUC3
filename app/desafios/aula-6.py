import locale, os, time

locale.setlocale(locale.LC_NUMERIC, 'pt_BR.UTF-8')
def format_currency(amount):
    formatted = '{:,.2f}'.format(amount)
    return 'R$ ' + formatted.replace(',', 'X').replace('.', ',').replace('X', '.')

CLIENTS = {} #client structure | CPF : Client()
ACCOUNTS = {}

class Client:
    def __init__(self,cpf,name):
        self.cpf = cpf
        self.name = name
        CLIENTS[self.cpf] = self
        self.has_account = False
    def new_account(self,type):
        result = True
        match type:
            case '0':
                SavingsAccount(self)
            case '1':
                CheckingAccount(self,100)
            case '2':
                CheckingAccount(self,400)
            case '3':
                CheckingAccount(self,800)
            case '4':
                CheckingAccount(self,1200)
            case '5':
                CheckingAccount(self,2000)
            case _:
                result = False
                print('ERRO: Valor inválido!')
                input('\nInsira para continuar => ')
        self.has_account = result
        return result
    def deposit(self):
        print('Quanto deseja depositar?\n')
        str_n = input('- R$ ')
        try:
            num = float(str_n.replace('.','').replace(',','.'))
            ACCOUNTS[self.cpf].deposit(num)
            print(f'{format_currency(num)} depositados!')
        except:
            print('ERRO: Valor inválido!')
            input('\nInsira para continuar => ')
    def withdraw(self):
        print('Quanto deseja sacar?\n')
        str_n = input('- R$ ')
        try:
            num = float(str_n.replace('.','').replace(',','.'))
            match ACCOUNTS[self.cpf].withdraw(num):
                case 0:
                    print(f'{format_currency(num)} retirados!')
                case 1:
                    print('Saldo insuficiente')
                case 2:
                    print('Valor acima do limite')
                case _:
                    print('?????????????????')
            input('\nInsira para continuar => ')
        except:
            print('ERRO: Valor inválido!')
            input('\nInsira para continuar => ')
    def check(self,account=False):
        if account and self.has_account:
            ACCOUNTS[self.cpf].check()
        else:
            print(self)
    def __str__(self):
        string =  f'  _____ ___ __ _ _ _  _  _   _    \n'
        string += f' |       U S U Á R I O            \n'
        string += f'/‾‾‾‾‾‾ ‾‾‾ ‾‾ ‾ ‾ ‾  ‾  ‾   ‾     ‾      \n'
        string += f'|   Nome: {self.name}              \n'
        string += f'|   CPF : {self.cpf}               \n'
        string += f'\\______ ___ __ _ _ _  _  _   _     _'
        return string

class Account:
    TYPE = '???'
    DICT = {'checking':'Corrente','savings':'Poupança','???':'!ERRO!'}
    def __init__(self, holder=Client):
        global ACCOUNTS
        self.index = holder.cpf
        self.holder= holder
        self.limit = None
        self.balance = float(0)
        ACCOUNTS[self.index] = self
    def deposit(self,n):
        self.balance += n
    def withdraw(self,n):
        if n <= self.balance:
            self.balance -= n
            return 0
        else:
            return 1
    def check(self):
        print(self)
    def __str__(self):
        string  = f'/‾‾‾‾‾‾ ‾‾‾ ‾‾ ‾ ‾ ‾  ‾  ‾   ‾     ‾      \n'
        string += f'|   Nome: {self.holder.name}              \n'
        string += f'|   CPF : {self.holder.cpf}               \n'
        string += f'|                                         \n'
        string += f'\\       C O N T A                        \n'
        string += f' |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ‾‾ ‾ ‾ ‾  ‾  ‾   ‾\n'
        string += f' |  Tipo  : {self.DICT[self.TYPE]}\n'
        string += f' |  Saldo : {format_currency(self.balance)}\n'
        if self.TYPE == 'checking':
            string += f' |  Limite: {format_currency(self.limit)}\n'
        string += f' \\____________________ __ _ _ _  _  _   _'

        return string

class CheckingAccount(Account):
    TYPE = 'checking'
    def __init__(self, holder, limit):
        super().__init__(holder)
        self.limit = float(limit)
        #limit
    def withdraw(self, n):
        if n <= self.limit:
            return super().withdraw(n)
        else:
            return 2

class SavingsAccount(Account):
    TYPE = 'savings'
    def __init__(self, holder):
        super().__init__(holder)
        #no limit

running = True
client = None
account = False
command = '0'

while running:
    os.system('cls')
    if type(client) == Client:
        client.check(account)

        print('Selecione um COMANDO:\n')
        if client.has_account:
            print('0. ocultar conta' if account else '0. mostrar conta')
            print('1. depositar dinheiro')
            print('2. sacar dinheiro')
            print('3. finalizar sessão')
            command = input('\n=> ')
            os.system('cls')
            match command:
                case '0':
                    account = not account
                case '1':
                    client.deposit()
                case '2':
                    client.withdraw()
                case '3':
                    running = False
                case _:
                    pass
        else:
            print('0. criar conta poupança')
            print('1. criar conta corrente')
            print('2. finalizar sessão')
            command = input('\n=> ')
            match command:
                case '0':
                    if client.new_account('0'):
                        print('\n Conta criada com sucesso!')
                        input('\n Insira para continuar => ')
                case '1':
                    os.system('cls')
                    print('Selecione um limite para sua conta:\n')
                    print('0. Cancelar')
                    print('1. R$   100,00')
                    print('2. R$   400,00')
                    print('3. R$   800,00')
                    print('4. R$ 1.200,00')
                    print('5. R$ 2.000,00')
                    limit = input('\n=> ')
                    if limit != '0':
                        if client.new_account(limit):
                            print('\n Conta criada com sucesso!')
                            input('\n Insira para continuar => ')
                case '2':
                    running = False 
                case _:
                    pass
    else:
        print('Para fazer login ou registrar-se, insira seu nome e cpf:')
        name = input(' - nome: ')
        cpf  = input(' - cpf : ')
        if cpf in CLIENTS:
            if CLIENTS[cpf].name == name:
                client = CLIENTS[cpf]
            else:
                pass
        else:
            CLIENTS[cpf] = Client(cpf,name)
            client =  CLIENTS[cpf]
        