from io import StringIO
from tkinter import *
from functools import partial
from turtle import right
from types import TracebackType
from database import SQL
from classes import *
db = SQL()

tela = Tk()
tela.geometry("500x550")
tela.minsize(550, 550)
tela.maxsize(550, 550)
tela.title('Sistema de matrícula.')

###TELA INICIAL###

telaInicial = Frame()


def inicial_login():
    telaInicial.pack_forget()
    tela_login.pack()


def inicial_cadastro():
    telaInicial.pack_forget()
    tela_cadastro.pack()


Label(telaInicial, text="Inicio", font='Arial 25 bold').pack(padx=15, pady=80)

Button(telaInicial, text="Login", font='Arial 11', command=inicial_login).pack(
    padx=10, pady=10, ipady=17, ipadx=42)
Button(telaInicial, text="Cadastro", font='Arial 11',
       command=inicial_cadastro).pack(padx=10, pady=10, ipady=17, ipadx=30)


###TELA SELEÇÃO DE CADASTRO###

tela_cadastro = Frame()


def Cadastro_cadastroAluno():
    tela_cadastro.pack_forget()
    tela_cadastro_aluno.pack()


def Cadastro_cadastroProfessor():
    tela_cadastro.pack_forget()
    tela_cadastroProfessor.pack()

Label(tela_cadastro,text="", font='Arial 11', padx=0, pady=66).pack()

Button(tela_cadastro, text="Cadastrar um Aluno", font='Arial 11',
       command=Cadastro_cadastroAluno).pack(padx=20, pady=20, ipady=17, ipadx=42)
Button(tela_cadastro, text="Cadastrar um Professor", font='Arial 11',
       command=Cadastro_cadastroProfessor).pack(padx=20, pady=20, ipady=17, ipadx=30)


#######TELA LOGADO (ALUNO) #######
tela_perfil_aluno = Frame()

nome_alu = StringVar()
cpf_alu = StringVar()
email_alu = StringVar()
sexo_alu = StringVar()
curso_alu = StringVar()

# #titulo
Label(tela_perfil_aluno, text="Perfil Aluno", font='Arial 16 bold', padx=0, pady=30).pack()
# #dados
Label(tela_perfil_aluno, textvariable = nome_alu, font='Arial 11', padx=0, pady=10).pack()
Label(tela_perfil_aluno, textvariable = cpf_alu, font='Arial 11', padx=0, pady=10).pack()
Label(tela_perfil_aluno, textvariable = email_alu, font='Arial 11', padx=0, pady=10).pack()
Label(tela_perfil_aluno, textvariable = sexo_alu, font='Arial 11', padx=0, pady=10).pack()
Label(tela_perfil_aluno, textvariable = curso_alu, font='Arial 11', padx=0, pady=10).pack()



#######TELA LOGADO (PROFESSOR) #######

tela_perfil_professor = Frame()

nome_prof = StringVar()
cpf_prof = StringVar()
email_prof = StringVar()
sexo_prof = StringVar()
formacao_prof = StringVar()
curso_prof = StringVar()

Label(tela_perfil_professor, text = "Perfil Professor", font='Arial 16 bold', padx=0, pady=30).pack()

Label(tela_perfil_professor, textvariable = nome_prof,font = 'Arial 11', padx=0, pady=10).pack()
Label(tela_perfil_professor, textvariable = cpf_prof,font = 'Arial 11', padx=0, pady=10).pack()
Label(tela_perfil_professor, textvariable = email_prof,font = 'Arial 11', padx=0, pady=10).pack()
Label(tela_perfil_professor, textvariable = sexo_prof,font = 'Arial 11', padx=0, pady=10).pack()
Label(tela_perfil_professor, textvariable = formacao_prof,font = 'Arial 11', padx=0, pady=10).pack()
Label(tela_perfil_professor, textvariable = curso_prof,font = 'Arial 11', padx=0, pady=10).pack()

### CADASTRO CURSO ###
tela_cadastro_curso= Frame()

def Cadastrar_curso(nome,professor):

    id_prof = db.Get_profid_by_nome(professor.get())

    output = db.Insert_Curso(nome.get(),id_prof)
    
    cadastro_curso_aviso.set(output)

def Prof_Curso():
    
    tela_perfil_professor.pack_forget()
    tela_cadastro_curso.pack()

Button(tela_perfil_professor, text="Cadastro Curso",
        font='Arial 11 bold', command=Prof_Curso).pack(side='right',padx=20, pady=10, ipady=4, ipadx=10)

Label(tela_cadastro_curso, text="Cadastrar Curso", font='Arial 16 bold', padx=0, pady=70).pack()

cadastro_curso_aviso = StringVar()
cadastro_curso_aviso.set("")
Label(tela_cadastro_curso, textvariable=cadastro_curso_aviso,font='Arial 11 bold', padx=0, pady=15).pack()

Label(tela_cadastro_curso, text="Digite o nome do curso: ", font='Arial 11',padx=0, pady=0).pack()

nome_curso_cadastrado = StringVar()
nome_curso_cadastrado.set("")
Entry(tela_cadastro_curso, textvariable = nome_curso_cadastrado, width=40).pack(padx=0, pady=10)


prof_a_cadastrar = StringVar()
prof_a_cadastrar.set("")
prof_a_cadastrar.set("Selecione o Professor: ")

lista_professor = db.Listar_professores()

prof1 = OptionMenu(tela_cadastro_curso, prof_a_cadastrar,*lista_professor)
prof1.pack(ipady=4, ipadx=25, pady=20)
prof1.config(font='Arial 11')

Cadastrar_curso = partial(Cadastrar_curso,nome_curso_cadastrado, prof_a_cadastrar)

Button(tela_cadastro_curso, text="Cadastrar",command=Cadastrar_curso, 
        font='Arial 11 bold',).pack(side='right',padx=20, pady=30, ipady=4, ipadx=20)



###TELA LOGIN###

tela_login = Frame()

login_aviso = StringVar()
login_aviso.set("")

def logar(cpf, ap):
    Verify = False

    if len(cpf.get()) != 11:
        login_aviso.set("CPF Inválido.")
        Verify = False
    elif ap.get() == "U":
        login_aviso.set("Selecione uma opção.")
        Verify = False
    else:
        Verificado = db.Verficar_login(cpf.get(),ap.get())
        Verify = True
    
    if Verify == True:
        if Verificado == "Aluno_V" or Verificado == "Professor_V":
            Verify = True
        elif Verificado == "Aluno_N":
            login_aviso.set("CPF não cadastrado como aluno.")
            Verify = False
        elif Verificado == "Professor_N":
            Verify = False
            login_aviso.set("CPF não cadastrado como professor.")

    if Verify == True:
        if ap.get()== "A":

            dados = db.Request_Aluno(cpf.get())

            tela_login.pack_forget()
            tela_perfil_aluno.pack()

            aluno = Aluno(dados[0],dados[1],dados[2],dados[3],dados[4])

            nome_alu.set("Nome: " + aluno.nome)
            cpf_alu.set("CPF: " + aluno.cpf)
            email_alu.set("Email: " + aluno.email)
            sexo_alu.set("Sexo: " + aluno.sexo)
            curso_alu.set("Curso: " + aluno.curso)

        elif ap.get()== "P":

            dados = db.Request_Professor(cpf.get())

            tela_login.pack_forget()
            tela_perfil_professor.pack()

            professor = Professor(dados[0],dados[1],dados[2],dados[3],dados[4])

            nome_prof.set("Nome: " + professor.nome)
            cpf_prof.set("CPF: " + professor.cpf)
            email_prof.set("Email: " + professor.email)
            sexo_prof.set("Sexo: " + professor.sexo)
            formacao_prof.set("Formação: " + professor.formacao)
        else:
            pass

Label(tela_login, text="Conecte-se com seu CPF.",
      font='Arial 15 bold', padx=0, pady=70).pack()

login_cpf = StringVar()
login_cpf.set("")
Entry(tela_login, textvariable=login_cpf, width=40).pack(padx=0, pady=20)


Label(tela_login, textvariable=login_aviso,
      font='Arial 11').pack()


Label(tela_login, text="Você é um Aluno ou Professor?",
      font='Arial 11', padx=0, pady=10).pack()

aluno_ou_professor = StringVar()
aluno_ou_professor.set("U")

logar = partial(logar, login_cpf, aluno_ou_professor)

Radiobutton(tela_login, text='Aluno', font='Arial 11',
                  variable=aluno_ou_professor, value='A', command=aluno_ou_professor).pack(padx=10, pady=10)

Radiobutton(tela_login, text='Professor', font='Arial 11',
                  variable=aluno_ou_professor, value='P', command=aluno_ou_professor).pack(padx=10, pady=10)

#BOTAO LOGIN#
Button(tela_login, text="Login", font='Arial 11 bold', command=logar).pack(
    side='right', padx=5, pady=1, ipady=4, ipadx=30)



###TELA CADASTRO ALUNO###
tela_cadastro_aluno = Frame()

nome = StringVar()
Label(tela_cadastro_aluno, text="Nome:",
      font='Arial 11', padx=0, pady=10).pack()
Entry(tela_cadastro_aluno, width=50, textvariable=nome).pack(padx=75)

cpf = StringVar()
Label(tela_cadastro_aluno, text="CPF:", font='Arial 11', padx=0, pady=10).pack()
Entry(tela_cadastro_aluno, width=50, textvariable=cpf).pack(padx=75)

email = StringVar()
Label(tela_cadastro_aluno, text="Email:",
      font='Arial 11', padx=0, pady=10).pack()
Entry(tela_cadastro_aluno, width=50, textvariable=email).pack(padx=75)


listacurso = db.Listar_cursos()

curso = StringVar()

curso.set("Selecionar o curso:")

curso1 = OptionMenu(tela_cadastro_aluno, curso, *listacurso)
curso1.pack(ipady=4, ipadx=25, pady=20)
curso1.config(font='Arial 11')

sexo_aluno = StringVar()
sexo_aluno.set("U")


Label(tela_cadastro_aluno, text="Sexo:",
      font='Arial 11', padx=0, pady=10).pack()

Radiobutton(tela_cadastro_aluno, text='Masculino', font='Arial 11',
            variable=sexo_aluno, value='M', command=sexo_aluno).pack(padx=10, pady=10)

Radiobutton(tela_cadastro_aluno, text='Feminino', font='Arial 11',
            variable=sexo_aluno, value='F', command=sexo_aluno).pack(padx=10, pady=10)


output_alu = StringVar()
output_alu.set("")

def output_aluno(nome, email, cpf, curso, sexo):
    try:
        cursoid = db.Get_cursoid_by_nome(curso.get())
    
        if sexo_aluno.get() == "U":
            msg = "Selecione um sexo."
        else:

            msg = db.Insert_Aluno(nome.get(), cpf.get(),
                                email.get(), sexo.get(), cursoid)
            if msg == "Cadastro realizado com sucesso!":
                nome.set("")
                cpf.set("")
                email.set("")
                sexo.set("U")
                curso.set("")
    except:
        msg = "Escolha um curso."
            
    output_alu.set(msg)

Label(tela_cadastro_aluno, textvariable=output_alu, font='Arial 11 bold', padx=0, pady=10).pack()

output_aluno = partial(output_aluno, nome, email, cpf, curso, sexo_aluno)

Button(tela_cadastro_aluno, text="OK",
        font='Arial 11 bold', command=output_aluno).pack(side='right', padx=75, pady=20, ipady=4, ipadx=24)



###TELA CADASTRO PROFESSOR###
tela_cadastroProfessor = Frame()

nome_pro = StringVar()
Label(tela_cadastroProfessor, text="Nome",
      font='Arial 11', padx=0, pady=10).pack()
Entry(tela_cadastroProfessor, width=50, textvariable=nome_pro).pack(padx=75)

cpf_pro = StringVar()
Label(tela_cadastroProfessor, text="CPF",
      font='Arial 11', padx=0, pady=10).pack()
Entry(tela_cadastroProfessor, textvariable=cpf_pro, width=50).pack(padx=75)

email_pro = StringVar()
Label(tela_cadastroProfessor, text="Email",
      font='Arial 11', padx=0, pady=10).pack()
Entry(tela_cadastroProfessor, width=50, textvariable=email_pro).pack(padx=75)

formacao_pro = StringVar()
Label(tela_cadastroProfessor, text="Formação",
      font='Arial 11', padx=0, pady=10).pack()
Entry(tela_cadastroProfessor, width=50, textvariable=formacao_pro).pack(padx=75)

sexo_pro = StringVar()
sexo_pro.set("U")

Label(tela_cadastroProfessor, text="Sexo:",
      font='Arial 11', padx=0, pady=10).pack()

Radiobutton(tela_cadastroProfessor, text='Masculino',
                  font='Arial 11', variable=sexo_pro, value='M', command=sexo_pro).pack(padx=10, pady=10)

Radiobutton(tela_cadastroProfessor, text='Feminino',
                  font='Arial 11', variable=sexo_pro, value='F', command=sexo_pro).pack(padx=10, pady=10)

professor_aviso = StringVar()
professor_aviso.set("")

def output_prof(nomepro, emailpro, cpfpro, formacaopro, sexopro):

    if sexopro.get() == "U":
        msg = "Selecione um sexo."
    else:
        msg = db.Insert_Professor(nomepro.get(), cpfpro.get(),
         emailpro.get(), sexopro.get(), formacaopro.get())
        if msg == "Cadastro realizado com sucesso!":
            nome_pro.set("")
            cpf_pro.set("")
            email_pro.set("")
            sexo_pro.set("U")
            formacao_pro.set("")
        

    professor_aviso.set(msg)


msg_prof = Label(tela_cadastroProfessor, textvariable=professor_aviso,
                 font='Arial 11 bold', padx=0, pady=10).pack()

output_prof = partial(output_prof, nome_pro, email_pro,
                      cpf_pro, formacao_pro, sexo_pro)

Button(tela_cadastroProfessor, text="OK",
        font='Arial 11 bold', command=output_prof).pack(side='right', padx=75, pady=20, ipady=4, ipadx=24)



###BOTAO DE VOLTAR###

def Voltar_inicio():

    tela_cadastro_aluno.pack_forget()
    tela_cadastroProfessor.pack_forget()
    tela_cadastro.pack_forget()
    tela_login.pack_forget()
    tela_perfil_aluno.pack_forget()
    tela_perfil_professor.pack_forget()
    tela_cadastro_curso.pack_forget()
    telaInicial.pack()


txt_voltar = "Voltar"

botao1 = Button(tela_cadastro, text=txt_voltar,
                font='Arial 11 bold', command=Voltar_inicio)
botao1.pack(side='bottom', padx=20, pady=30, ipady=4, ipadx=30)

Button(tela_cadastro_aluno, text=txt_voltar,
        font='Arial 11 bold', command=Voltar_inicio).pack(side='left', padx=75, pady=1, ipady=4, ipadx=30)


Button(tela_cadastroProfessor, text=txt_voltar,
        font='Arial 11 bold', command=Voltar_inicio).pack(side='left', padx=75, pady=1, ipady=4, ipadx=30)


Button(tela_login, text=txt_voltar,
        font='Arial 11 bold', command=Voltar_inicio).pack(side='left', padx=5, pady=1, ipady=4, ipadx=30)


Button(tela_perfil_professor, text=txt_voltar,
        font='Arial 11 bold', command=Voltar_inicio).pack(padx=20, pady=10, ipady=4, ipadx=30)


Button(tela_perfil_aluno, text=txt_voltar,
        font='Arial 11 bold', command=Voltar_inicio).pack(padx=5, pady=1, ipady=4, ipadx=30)


Button(tela_cadastro_curso, text=txt_voltar,
        font='Arial 11 bold', command=Voltar_inicio).pack(padx=20, pady=30, ipady=4, ipadx=30)



telaInicial.pack()
tela.mainloop()
