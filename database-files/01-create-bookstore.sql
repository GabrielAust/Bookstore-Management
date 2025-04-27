-- database-files/01-create-bookstore.sql
CREATE DATABASE IF NOT EXISTS bookstore;
USE bookstore;

-- 1) Categories
CREATE TABLE Category (
                          CategoryID    INT           AUTO_INCREMENT PRIMARY KEY,
                          Name          VARCHAR(255)  NOT NULL
);

-- 2) Vendors
CREATE TABLE Vendor (
                        VendorID      INT           AUTO_INCREMENT PRIMARY KEY,
                        VendorName    VARCHAR(255)  NOT NULL,
                        ContactInfo   VARCHAR(255)
);

-- 3) Customers
CREATE TABLE Customer (
                          CustomerID    INT           AUTO_INCREMENT PRIMARY KEY,
                          Name          VARCHAR(255)  NOT NULL,
                          Email         VARCHAR(255)  NOT NULL UNIQUE,
                          Password      VARCHAR(255)  NOT NULL
);

-- 4) Books
CREATE TABLE Book (
                      BookID        INT           AUTO_INCREMENT PRIMARY KEY,
                      Title         VARCHAR(255)  NOT NULL,
                      Author        VARCHAR(255),
                      ISBN          VARCHAR(20)   UNIQUE,
                      Price         DECIMAL(10,2) NOT NULL,
                      Description   TEXT,
                      CoverImage    VARCHAR(255),
                      CategoryID    INT,
                      VendorID      INT,
                      FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID),
                      FOREIGN KEY (VendorID)   REFERENCES Vendor(VendorID)
);

-- 5) Inventory (one row per book)
CREATE TABLE Inventory (
                           BookID            INT           PRIMARY KEY,
                           StockQuantity     INT           NOT NULL,
                           LastRestockedDate DATE,
                           FOREIGN KEY (BookID) REFERENCES Book(BookID)
);

-- 6) Orders
CREATE TABLE `Order` (
                         OrderID       INT           AUTO_INCREMENT PRIMARY KEY,
                         CustomerID    INT           NOT NULL,
                         OrderDate     DATETIME      DEFAULT CURRENT_TIMESTAMP,
                         Status        VARCHAR(50),
                         TotalAmount   DECIMAL(10,2),
                         FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

-- 7) OrderDetails (bridge table)
CREATE TABLE OrderDetail (
                             OrderID    INT           NOT NULL,
                             BookID     INT           NOT NULL,
                             Quantity   INT           NOT NULL,
                             Price      DECIMAL(10,2) NOT NULL,
                             PRIMARY KEY (OrderID, BookID),
                             FOREIGN KEY (OrderID) REFERENCES `Order`(OrderID),
                             FOREIGN KEY (BookID)  REFERENCES Book(BookID)
);
