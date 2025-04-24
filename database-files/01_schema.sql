CREATE DATABASE IF NOT EXISTS OnlineBookstoreDB;
USE OnlineBookstoreDB;

CREATE TABLE Category (
                          CategoryID INT AUTO_INCREMENT PRIMARY KEY,
                          Name VARCHAR(100) NOT NULL
);

CREATE TABLE Vendor (
                        VendorID INT AUTO_INCREMENT PRIMARY KEY,
                        VendorName VARCHAR(100) NOT NULL,
                        ContactInfo VARCHAR(255)
);

CREATE TABLE Book (
                      BookID INT AUTO_INCREMENT PRIMARY KEY,
                      Title VARCHAR(200) NOT NULL,
                      Author VARCHAR(100) NOT NULL,
                      ISBN VARCHAR(20) UNIQUE,
                      Price DECIMAL(8,2) NOT NULL,
                      Description TEXT,
                      CoverImage VARCHAR(255),
                      CategoryID INT,
                      VendorID INT,
                      FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID),
                      FOREIGN KEY (VendorID) REFERENCES Vendor(VendorID)
);

CREATE TABLE Customer (
                          CustomerID INT AUTO_INCREMENT PRIMARY KEY,
                          Name VARCHAR(100) NOT NULL,
                          Email VARCHAR(100) UNIQUE NOT NULL,
                          Password VARCHAR(100)
);

CREATE TABLE `Order` (
                         OrderID INT AUTO_INCREMENT PRIMARY KEY,
                         CustomerID INT,
                         OrderDate DATETIME DEFAULT CURRENT_TIMESTAMP,
                         Status VARCHAR(50),
                         TotalAmount DECIMAL(10,2),
                         FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

CREATE TABLE OrderDetail (
                             OrderID INT,
                             BookID INT,
                             Quantity INT DEFAULT 1,
                             Price DECIMAL(8,2),
                             PRIMARY KEY (OrderID, BookID),
                             FOREIGN KEY (OrderID) REFERENCES `Order`(OrderID),
                             FOREIGN KEY (BookID) REFERENCES Book(BookID)
);

CREATE TABLE Inventory (
                           BookID INT PRIMARY KEY,
                           StockQuantity INT DEFAULT 0,
                           LastRestockedDate DATE,
                           FOREIGN KEY (BookID) REFERENCES Book(BookID)
);
