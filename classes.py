class Usuario():
    def __init__(self, nome, cpf, email, sexo):
        self.nome = str(nome)
        self.cpf = str(cpf)
        self.email = str(email)
        self.sexo = str(sexo)

    def get_info(self):
        print(f'{self.nome},{self.cpf},{self.email},{self.sexo},{self.matricula}')

class Professor(Usuario):
    def __init__(self,nome, cpf, email, sexo, formacao):
        super().__init__(nome, cpf, email, sexo)
        self.formacao = formacao
        
    def info(self):
        print(self.nome,self.cpf,self.email,self.sexo,self.formacao)

class Aluno(Usuario):
    def __init__(self, nome, cpf, email, sexo,curso):
        super().__init__(nome, cpf, email, sexo)
        self.curso = curso

class Curso():
    def __init__(self, nome,coddocente):
        self.nome = nome
        self.coddocente = coddocente