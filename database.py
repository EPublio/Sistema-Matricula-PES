from classes import *
import mysql.connector

class SQL():
    def __init__(self):
        self.con = mysql.connector.connect(host='localhost',database='matricula',user='root',password='')

        if self.con.is_connected():
            self.db_info = self.con.get_server_info()
            self.cursor = self.con.cursor()
    
    def Select(self,tablename):
        sql = f"""SELECT * FROM {tablename}"""
        try:
            self.cursor.execute(sql)
            r = self.cursor.fetchall()
            for x in r:
                print(x)
        except:
            self.con.rollback()

    def Get_cursoid_by_nome(self,nomecurso):
        sql = f"SELECT cod FROM curso WHERE nome='{nomecurso}'"
        self.cursor.execute(sql)
    
        result = self.cursor.fetchall()

        for x in result:
            x = list(x)
            id = x[0]

        return id

    def Get_profid_by_nome(self,nomeprof):
        sql = f"SELECT cod FROM professor WHERE nome='{nomeprof}'"
        self.cursor.execute(sql)
    
        result = self.cursor.fetchall()

        for x in result:
            x = list(x)
            id = x[0]

        return id

    def Listar_cursos(self):
        lista_cursos = []
        sql = f"""SELECT nome FROM curso"""
        try:
            self.cursor.execute(sql)
            r = self.cursor.fetchall()
            for x in r:
                for y in x:
                    lista_cursos.append(y)
        except:
            self.con.rollback()
        return lista_cursos

    def Listar_professores(self):
        lista_profs = []
        sql = f"""SELECT nome FROM professor"""
        try:
            self.cursor.execute(sql)
            r = self.cursor.fetchall()
            for x in r:
                for y in x:
                    lista_profs.append(y)
        except:
            self.con.rollback()
        return lista_profs

    def Insert_Professor(self,nome, cpf, email, sexo, formacao) :
        sql = f"""INSERT INTO professor(nome,cpf,email,sexo,formacao)VALUES('{nome}','{cpf}','{email}','{sexo}','{formacao}')"""
        continuar = True    

        try:
            int(cpf)
        except ValueError:
            output = "CPF deve ter apenas números."
            continuar = False
    
        #verifica a quantidade maxima de caracteres
        if continuar == True:
            if len(nome) > 150:
                continuar = False
                output = "Nome ultrapassa a quantidade máxima de caractéres."
            elif len(nome) < 10:
                output = "Nome inválido."
                continuar = False
            elif len(email) < 5:
                continuar = False
                output = "Email inválido."
            elif len(str(cpf)) != 11:
                continuar = False
                output = "CPF inválido."
            elif len(email) > 75:
                continuar = False
                output = "Email ultrapassa a quantidade máxima de caractéres."
            elif len(email) < 5:
                continuar = False
                output = "Email inválido."
            elif "@" not in email or " " in email:
                continuar = False
                output = "Email inválido"
            elif len(formacao) > 50 or len(formacao) <= 5:
                continuar = False
                output = "Formação não contém a quantidade de caractéres adequada."
                
            
        #verifica cpf duplicado
        if continuar == True:
            find_cpf = f"""SELECT cpf FROM professor WHERE cpf={cpf}"""
            self.cursor.execute(find_cpf)
            result_cpf = self.cursor.fetchall()
        
            for x in list(result_cpf) :
                for y in x:
                    if int(y) == cpf:
                        output = "CPF já cadastrado."
                        continuar = False
        #verifica email duplicado
        if continuar == True :
            find_email = f"""SELECT email FROM professor WHERE email='{email}'"""
            self.cursor.execute(find_email)
            result_email = self.cursor.fetchall()

            for x in result_email:
                for y in x:
                    if str(y) == email:
                        output = "Email já cadastrado."
                        continuar = False
    
        # ULTIMO IF DE INSERT
        if continuar == True:
            try:
                self.cursor.execute(sql)
                self.con.commit()
            except mysql.connector.Error as err:
                self.con.rollback()
                continuar = False
                output = str(err)

        if continuar == True:
            output = "Cadastro realizado com sucesso!"
        return output
    
    def Insert_Curso(self,nome,coddocente):
        sql = f"INSERT INTO curso(nome,coddocente)VALUES('{nome}','{coddocente}')"
        continuar = True
        output = ""
        if len(nome) < 5 or len(nome) > 100 :
            output = "Nome de curso inválido."
            continuar = False
        
        if continuar == True :   
            find_curso = f"""SELECT curso.nome FROM curso WHERE curso.nome='{nome}'"""
            self.cursor.execute(find_curso)
            result_cursos = self.cursor.fetchall()
            for x in result_cursos:
                if nome in x :
                    output = "Curso já cadastrado."
                    continuar = False

        if continuar == True:
            try:
                self.cursor.execute(sql)
                self.con.commit()
                output = "Seu curso foi cadastrado!"
            except mysql.connector.Error as err:
                self.con.rollback()
                output = str(err)

        return output

    def Insert_Aluno(self,nome, cpf, email, sexo, curso) :
        sql = f"INSERT INTO aluno(nome,cpf,email,sexo,curso)VALUES('{nome}','{cpf}','{email}','{sexo}','{curso}')"
        continuar = True    

        try:
            int(cpf)
        except ValueError:
            output = "CPF deve ter apenas números."
            continuar = False
    
        #verifica a quantidade maxima de caracteres
        if continuar == True:
            if len(nome) > 150:
                continuar = False
                output = "Nome ultrapassa a quantidade máxima de caractéres."
            elif len(nome) < 10:
                output = "Nome inválido."
                continuar = False
            elif len(email) < 5:
                continuar = False
                output = "Email inválido."
            elif len(str(cpf)) != 11:
                continuar = False
                output = "CPF inválido."
            elif len(email) > 75:
                continuar = False
                output = "Email ultrapassa a quantidade máxima de caractéres."
            elif "@" not in email or " " in email:
                continuar = False
                output = "Email inválido"


        #verifica cpf duplicado
        if continuar == True:
            find_cpf = f"""SELECT cpf FROM professor WHERE cpf={cpf}"""
            self.cursor.execute(find_cpf)
            result_cpf = self.cursor.fetchall()
        
            for x in list(result_cpf) :
                for y in x:
                    if int(y) == cpf:
                        output = "CPF já cadastrado."
                        continuar = False
        #verifica email duplicado
        if continuar == True :
            find_email = f"""SELECT email FROM professor WHERE email='{email}'"""
            self.cursor.execute(find_email)
            result_email = self.cursor.fetchall()

            for x in result_email:
                for y in x:
                    if str(y) == email:
                        output = "Email já cadastrado."
                        continuar = False
    
        if continuar == True:
            try:
                self.cursor.execute(sql)
                self.con.commit()
                output = "Cadastro realizado com sucesso!"
            except mysql.connector.Error as err:
                print(err)
                self.con.rollback()
                output = str(err)
        return output

    def Request_Aluno(self,cpf):
        sql = f"""SELECT aluno.nome,aluno.cpf,aluno.email,aluno.sexo,curso.nome 
                FROM aluno,curso 
                WHERE aluno.curso = curso.cod AND cpf={cpf}"""

        cpfs = f"SELECT aluno.cpf FROM aluno"
        
        try:
            self.cursor.execute(cpfs)
            lista_cpfs = self.cursor.fetchall()
            lista = [item for sublista in lista_cpfs for item in sublista]
            if cpf in lista:
                try:
                    self.cursor.execute(sql)
                    dados_usuario = self.cursor.fetchall()
                except:
                    self.con.rollback()
                dados_usuario = list(dados_usuario[0])
            else:
                dados_usuario = ["Erro","Erro","Erro","Erro","Erro"]
        except:
            self.con.rollback()
        return dados_usuario

    def Request_Professor(self, cpf):
        sql = f"""SELECT professor.nome, professor.cpf, professor.email, professor.sexo, professor.formacao
            FROM professor
            WHERE professor.cpf ={cpf}"""

        cpfs = f"SELECT professor.cpf FROM professor"

        curso = f"SELECT curso.nome FROM curso, professor WHERE curso.cod = professor.cod AND professor.cpf ={cpf}"

        try:
            self.cursor.execute(cpfs)
            lista_cpfs = self.cursor.fetchall()
            lista = [item for sublista in lista_cpfs for item in sublista]
            if cpf in lista:
                try:
                    self.cursor.execute(sql)
                    dados_usuario = self.cursor.fetchall()
                    try:
                        self.cursor.execute(curso)
                        curso = self.cursor.fetchall()
                        if curso == []:
                            curso_prof = "Não cadastrado."
                        else:
                            curso_prof = curso[0][0]
                    except:
                        self.con.rollback()
                except:
                    self.con.rollback()
                dados_usuario = list(dados_usuario[0])
                dados_usuario.append(curso_prof)
            else:
                dados_usuario = ["Erro","Erro","Erro","Erro","Erro"]
        except:
            self.con.rollback()
        return dados_usuario

    def Verficar_login(self,cpf,ap):

        output = ""
        if ap == "A":
            sql = f"SELECT aluno.cpf FROM aluno WHERE cpf={cpf}"
            try:
                self.cursor.execute(sql)
                result = self.cursor.fetchall()
                lista = [item for sublista in result for item in sublista]
                if lista[0] == cpf:
                    output = "Aluno_V"
            except:
                output = "Aluno_N"
            
        elif ap == "P":
            sql = f"SELECT professor.cpf FROM professor WHERE cpf={cpf}"
            try:
                self.cursor.execute(sql)
                result = self.cursor.fetchall()
                lista = [item for sublista in result for item in sublista]
                if lista[0] == cpf:
                    output = "Professor_V"
            except:
                output = "Professor_N"

        return output   