from faker import Faker
import random

fake = Faker()

def generate_categories(n=30):
    for _ in range(n):
        name = fake.unique.word().capitalize().replace("'", "''")
        print(f"INSERT INTO Category (Name) VALUES ('{name}');")

def generate_vendors(n=30):
    for _ in range(n):
        vendor = fake.company().replace("'", "''")
        contact = fake.company_email()
        print(f"INSERT INTO Vendor (VendorName, ContactInfo) VALUES ('{vendor}', '{contact}');")

def generate_books(n=40, cat_count=30, vend_count=30):
    for _ in range(n):
        title = fake.sentence(nb_words=3).replace("'", "''")
        author = fake.name().replace("'", "''")
        isbn = fake.isbn13(separator="")
        price = round(random.uniform(5, 50), 2)
        desc = fake.text(max_nb_chars=100).replace("'", "''")
        cover = fake.file_name(extension="jpg")
        cat = random.randint(1, cat_count)
        vend = random.randint(1, vend_count)
        print(f"INSERT INTO Book (Title, Author, ISBN, Price, Description, CoverImage, CategoryID, VendorID) VALUES ('{title}', '{author}', '{isbn}', {price}, '{desc}', '{cover}', {cat}, {vend});")

def generate_customers(n=40):
    for _ in range(n):
        name = fake.name().replace("'", "''")
        email = fake.email()
        pw = fake.password(length=12)
        print(f"INSERT INTO Customer (Name, Email, Password) VALUES ('{name}', '{email}', '{pw}');")

def generate_orders(n=75, cust_count=40):
    statuses = ['Processing','Shipped','Delivered','Cancelled']
    for _ in range(n):
        cust = random.randint(1, cust_count)
        status = random.choice(statuses)
        total = round(random.uniform(10, 200), 2)
        date = fake.date_between(start_date='-6m', end_date='today')
        print(f"INSERT INTO `Order` (CustomerID, Status, TotalAmount, OrderDate) VALUES ({cust}, '{status}', {total}, '{date}');")

def generate_order_details(n=125, order_count=75, book_count=40):
    for _ in range(n):
        oid = random.randint(1, order_count)
        bid = random.randint(1, book_count)
        qty = random.randint(1, 5)
        price = round(random.uniform(5, 50), 2)
        print(f"INSERT INTO OrderDetail (OrderID, BookID, Quantity, Price) VALUES ({oid}, {bid}, {qty}, {price});")

def generate_inventory(book_count=40):
    for bid in range(1, book_count+1):
        qty = random.randint(0, 100)
        date = fake.date_between(start_date='-3m', end_date='today')
        print(f"INSERT INTO Inventory (BookID, StockQuantity, LastRestockedDate) VALUES ({bid}, {qty}, '{date}');")

if __name__ == "__main__":
    print("-- Categories")
    generate_categories()
    print("\n-- Vendors")
    generate_vendors()
    print("\n-- Books")
    generate_books()
    print("\n-- Customers")
    generate_customers()
    print("\n-- Orders")
    generate_orders()
    print("\n-- OrderDetails")
    generate_order_details()
    print("\n-- Inventory")
    generate_inventory()

