import pyodbc

DROP  TABLE IF EXISTS Produit 
CREATE TABLE Produit(
	CodeProduit int primary key,
	Nom VARCHAR(50)not null,
	Descriptions VARCHAR(200),
	StockActuel INTEGER not null,
	PrixUnitaire FLOAT not null,
	CodeCategorie int not null,
)
