DROP DATABASE IF EXISTS hospital_db;

create DATABASE hospital_db;

use hospital_db;

CREATE TABLE `cargos` (
  `Id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `Designacao` VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE `utilizador` (
  `Id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `Username` VARCHAR(80) UNIQUE NOT NULL,
  `Password` VARCHAR(255) NOT NULL,
  `Cargos` INTEGER NOT NULL,
  `Nome` VARCHAR(100) NOT NULL,
  `Email` VARCHAR(100) UNIQUE,
  `Telefone` VARCHAR(20),
  `DataCriacao` DATETIME NOT NULL DEFAULT (CURRENT_TIMESTAMP),
  FOREIGN KEY (`Cargos`) REFERENCES `cargos` (`Id`) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE `stock` (
  `Id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `Nome` VARCHAR(100) UNIQUE NOT NULL,
  `Quantidade` INTEGER NOT NULL DEFAULT 0,
  `QuantidadeMinima` INTEGER NOT NULL DEFAULT 5,
  `Descricao` VARCHAR(200)
);

CREATE TABLE `reportados_stock` (
  `Id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `IdStock` INTEGER NOT NULL,
  `IdReporter` INTEGER,
  `DataReporte` DATETIME NOT NULL DEFAULT (CURRENT_TIMESTAMP),
  `QuantidadeAtual` INTEGER NOT NULL,
  `Descricao` VARCHAR(300),
  `Estado` VARCHAR(30) NOT NULL DEFAULT 'Pendente',
  FOREIGN KEY (`IdStock`) REFERENCES `stock` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`IdReporter`) REFERENCES `utilizador` (`Id`) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE `avarias` (
  `Id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `IdReporter` INTEGER NOT NULL,
  `DataReporte` DATETIME NOT NULL DEFAULT (CURRENT_TIMESTAMP),
  `Descricao` VARCHAR(500) NOT NULL,
  `Localizacao` VARCHAR(100),
  `Estado` VARCHAR(30) NOT NULL DEFAULT 'Pendente',
  `IdTecnico` INTEGER,
  FOREIGN KEY (`IdReporter`) REFERENCES `utilizador` (`Id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`IdTecnico`) REFERENCES `utilizador` (`Id`) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE `consultas` (
  `Id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `Data` DATE NOT NULL,
  `Hora` TIME NOT NULL,
  `IdUtente` INTEGER NOT NULL,
  `IdMedico` INTEGER NOT NULL,
  `TipoConsulta` VARCHAR(50) NOT NULL,
  `Estado` VARCHAR(30) NOT NULL DEFAULT 'Marcada',
  `Observacoes` VARCHAR(500),
  FOREIGN KEY (`IdUtente`) REFERENCES `utilizador` (`Id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`IdMedico`) REFERENCES `utilizador` (`Id`) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE `cirurgias` (
  `Id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `Data` DATE NOT NULL,
  `Hora` TIME NOT NULL,
  `IdUtente` INTEGER NOT NULL,
  `IdCirurgiaoPrincipal` INTEGER NOT NULL,
  `DuracaoEstimada` INTEGER NOT NULL,
  `TipoCirurgia` VARCHAR(100) NOT NULL,
  `Estado` VARCHAR(30) NOT NULL DEFAULT 'Marcada',
  `Observacoes` VARCHAR(500),
  FOREIGN KEY (`IdUtente`) REFERENCES `utilizador` (`Id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`IdCirurgiaoPrincipal`) REFERENCES `utilizador` (`Id`) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE `assistentes_cirurgia` (
  `IdCirurgia` INTEGER NOT NULL,
  `IdMedico` INTEGER NOT NULL,
  PRIMARY KEY (`IdCirurgia`, `IdMedico`),
  FOREIGN KEY (`IdCirurgia`) REFERENCES `cirurgias` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`IdMedico`) REFERENCES `utilizador` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE `medicamentos` (
  `Id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `Nome` VARCHAR(100) UNIQUE NOT NULL,
  `Descricao` VARCHAR(300)
);

CREATE TABLE `receitas` (
  `Id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `IdUtente` INTEGER NOT NULL,
  `IdConsulta` INTEGER NOT NULL,
  `DataCriacao` DATETIME NOT NULL DEFAULT (CURRENT_TIMESTAMP),
  FOREIGN KEY (`IdUtente`) REFERENCES `utilizador` (`Id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`IdConsulta`) REFERENCES `consultas` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE `receitas_medicamentos` (
  `Id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `IdReceita` INTEGER NOT NULL,
  `IdMedicamento` INTEGER NOT NULL,
  `Observacoes` VARCHAR(400),
  `DataInicio` DATE NOT NULL,
  `DataFim` DATE,
  FOREIGN KEY (`IdReceita`) REFERENCES `receitas` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`IdMedicamento`) REFERENCES `medicamentos` (`Id`) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE `mensagens` (
  `Id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `IdRemetente` INTEGER NOT NULL,
  `IdDestinatario` INTEGER NOT NULL,
  `DataEnvio` DATETIME NOT NULL DEFAULT (CURRENT_TIMESTAMP),
  `Conteudo` TEXT NOT NULL,
  `Lida` BOOLEAN NOT NULL DEFAULT false,
  FOREIGN KEY (`IdRemetente`) REFERENCES `utilizador` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`IdDestinatario`) REFERENCES `utilizador` (`Id`) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO `cargos`(`Id`,`Designacao`) VALUES(1,'medico');
INSERT INTO `cargos`(`Id`,`Designacao`) VALUES(2,'utente');
INSERT INTO `cargos`(`Id`,`Designacao`) VALUES(3,'administrador');
INSERT INTO `utilizador`(`Id`,`Username`,`Password`,`Cargos`,`Nome`,`Email`,`Telefone`,`DataCriacao`) VALUES(1,'jose','jose123',1,'José Rajão','joserajao@gmail.com','945873123','2026-03-06 05:17:44');
INSERT INTO `utilizador`(`Id`,`Username`,`Password`,`Cargos`,`Nome`,`Email`,`Telefone`,`DataCriacao`) VALUES(2,'daniel','daniel123',2,'Daniel Magalhães','danielmagalhaes@gmail.com','983245876','2026-03-22 17:10:22');
INSERT INTO `utilizador`(`Id`,`Username`,`Password`,`Cargos`,`Nome`,`Email`,`Telefone`,`DataCriacao`) VALUES(3,'almeida','almeida266',3,'Francisco Almeida','franciscoalmeida@gmail.com','945876324','2026-03-23 13:06:18');
INSERT INTO `consultas`(`Id`,`Data`,`Hora`,`IdUtente`,`IdMedico`,`TipoConsulta`,`Estado`,`Observacoes`) VALUES(1,'2026-03-27','16:00:00',2,1,'Dermatologia','Marcada','Trazer as analises ao sangue ');
INSERT INTO `consultas`(`Id`,`Data`,`Hora`,`IdUtente`,`IdMedico`,`TipoConsulta`,`Estado`) VALUES(2,'2026-03-18','09:30:00',2,1,'Rotina','Marcada');
INSERT INTO `medicamentos`(`Id`,`Nome`,`Descricao`) VALUES(1,'Ben-u-ron','Medicamento para as dores ');
INSERT INTO `medicamentos`(`Id`,`Nome`,`Descricao`) VALUES(2,'Ibuprofeno','Anti-inflamatório para o alívio da dor');