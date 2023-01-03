CREATE DATABASE matricula;

USE matricula;

CREATE TABLE IF NOT EXISTS professor(
	cod INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(150) NOT NULL,
	cpf CHAR(11) NOT NULL,
	email VARCHAR(50) NOT NULL,
	sexo CHAR(1) NOT NULL,
	formacao VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS curso(
	cod INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	coddocente INT NOT NULL,
	FOREIGN KEY (coddocente) REFERENCES professor(cod) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS aluno(
	cod INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(150) NOT NULL,
	cpf CHAR(11) NOT NULL,
	email VARCHAR(50) NOT NULL,
	sexo CHAR(1) NOT NULL,
	curso INT NOT NULL,
	FOREIGN KEY (curso) REFERENCES curso(cod) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO professor(nome,cpf,email,sexo,formacao)VALUES
("professor teste 1","65464578657","emailteste@gmail.com","M","formação 1"),
("professor teste 2","87687687686","emailteste2@gmail.com","F","formação teste 2");

INSERT INTO curso(nome,coddocente)VALUES
("Curso teste 1", 1),
("Curso teste 2", 2),
("Curso teste 3", 1);

INSERT INTO aluno(nome,cpf,email,sexo,curso) VALUES
("Aluno teste nome 1", "31231232312","alunoemail@gmail.com","F", 1),
("Aluno teste nome 2", "23423423443","alunoemail2@gmail.com","M", 3),
("Aluno teste nome 3", "54354354334","alunoemail3@gmail.com","F", 2);