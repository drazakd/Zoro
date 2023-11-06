CREATE DATABASE product

CREATE TABLE Magasin(
IdMagasin INT IDENTITY(1,1) PRIMARY KEY,
Nom VARCHAR(50),
Adresse VARCHAR(100),
Telephone VARCHAR(15),
Email VARCHAR(75)
);

CREATE TABLE Produit (
CodeProduit INT IDENTITY(1,1) PRIMARY KEY,
Nom VARCHAR(50),
Description VARCHAR(200),
PrixUnitaire FLOAT,
);

CREATE TABLE Vente(
IdVente INT PRIMARY KEY IDENTITY(1,1),
Quantite INT NOT NULL,
PrixTotal FLOAT NOT NULL,
CodeProduit INT,
FOREIGN KEY (CodeProduit) REFERENCES Produit(CodeProduit),
IdMagasin INT,
FOREIGN KEY (IdMagasin) REFERENCES Magasin(IdMagasin)
<<<<<<< Updated upstream
);
=======
);
>>>>>>> Stashed changes
