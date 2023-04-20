# Getting errors creating tables with foreign keys
# suppliers_table_string = '''
#                         CREATE TABLE IF NOT EXISTS Suppliers(
#                         id INT(3) ZEROFILL NOT NULL AUTO_INCREMENT,
#                         Name VARCHAR(50),
#                         Balance DECIMAL(18,2),
#                         PRIMARY KEY(id))
#                         '''

# items_table_string = '''
#                         CREATE TABLE IF NOT EXISTS Items(
#                         id INT(3) ZEROFILL NOT NULL AUTO_INCREMENT,
#                         Name VARCHAR(50),
#                         SalePrice DECIMAL(18,2),
#                         PriorInventory INT,
#                         PRIMARY KEY(id))
#                         '''
# purchasers_table_string = '''
#                         CREATE TABLE IF NOT EXISTS Purchasers(
#                         id INT(3) ZEROFILL NOT NULL AUTO_INCREMENT,
#                         Name VARCHAR(50),
#                         Balance DECIMAL(18,2),
#                         PRIMARY KEY(id))
#                         '''

# supplierPrices_table_string = '''
#                         CREATE TABLE IF NOT EXISTS SupplierPrices(
#                         SupplierID INT(3) ZEROFILL,
#                         ItemID INT(3) ZEROFILL,
#                         SuppleirPrice DECIMAL(18,2),
#                         PRIMARY KEY(SupplierID, ItemID),
#                         constraint sp_supplier_fk FOREIGN KEY (SupplierID) REFERENCES Suppliers(id),
#                         constraint sp_item_fk FOREIGN KEY (ItemID) REFERENCES Items(id)
#                         )'''

# sales_table_string = '''
#                         CREATE TABLE IF NOT EXISTS Sales(
#                         id INT(3) ZEROFILL NOT NULL AUTO_INCREMENT,
#                         PurchaserID INT(3) ZEROFILL,
#                         ItemID INT(3) ZEROFILL,
#                         Quantity INT,
#                         TotalSalePrice DECIMAL(18,2),
#                         InvoiceDate DATE,
#                         PayDate DATE,
#                         SaleDate DATE,
#                         ShipDate DATE,
#                         PRIMARY KEY(id)),
#                         constraint sales_purchaser_fk FOREIGN KEY (PurchaserID) REFERENCES Purchasers(id),
#                         constraint sales_item_fk FOREIGN KEY (ItemID) REFERENCES Items(id)
#                         )'''

# orders_table_string = '''
#                         CREATE TABLE IF NOT EXISTS Orders(
#                         id INT(3) ZEROFILL NOT NULL AUTO_INCREMENT,
#                         SupplierID INT(3) ZEROFILL,
#                         ItemID INT(3) ZEROFILL,
#                         Quantity INT,
#                         TotalOrderPrice DECIMAL(18,2),
#                         InvoiceDate DATE,
#                         PayDate DATE,
#                         OrderDate DATE,
#                         RecieveDate DATE,
#                         PRIMARY KEY(id),
#                         constraint orders_supplier_fk FOREIGN KEY (SupplierID) REFERENCES Suppliers(id),
#                         constraint orders_item_fk FOREIGN KEY (ItemID) REFERENCES Items(id)
#                         )'''

# table_strings = [suppliers_table_string, items_table_string, purchasers_table_string, supplierPrices_table_string, sales_table_string, orders_table_string]

# drop_table_string = '''
#                     SET foreign_key_checks = 0;
#                     DROP TABLE IF EXISTS Suppliers;
#                     DROP TABLE IF EXISTS Items;
#                     DROP TABLE IF EXISTS Purchasers;
#                     DROP TABLE IF EXISTS SupplierPrices;
#                     DROP TABLE IF EXISTS Sales;
#                     DROP TABLE IF EXISTS Orders;
#                     SET foreign_key_checks = 0;


suppliers_table_string = '''
                        CREATE TABLE IF NOT EXISTS Suppliers(
                        id INT(3) ZEROFILL NOT NULL AUTO_INCREMENT,
                        Name VARCHAR(50),
                        Balance DECIMAL(18,2),
                        PRIMARY KEY(id))
                        '''

items_table_string = '''
                        CREATE TABLE IF NOT EXISTS Items(
                        id INT(3) ZEROFILL NOT NULL AUTO_INCREMENT,
                        Name VARCHAR(50),
                        SalePrice DECIMAL(18,2),
                        PriorInventory INT,
                        PRIMARY KEY(id))
                        '''
purchasers_table_string = '''
                        CREATE TABLE IF NOT EXISTS Purchasers(
                        id INT(3) ZEROFILL NOT NULL AUTO_INCREMENT,
                        Name VARCHAR(50),
                        Balance DECIMAL(18,2),
                        PRIMARY KEY(id))
                        '''

supplierPrices_table_string = '''
                        CREATE TABLE IF NOT EXISTS SupplierPrices(
                        SupplierID INT(3) ZEROFILL,
                        ItemID INT(3) ZEROFILL,
                        SuppleirPrice DECIMAL(18,2),
                        PRIMARY KEY(SupplierID, ItemID)
                        )'''

sales_table_string = '''
                        CREATE TABLE IF NOT EXISTS Sales(
                        id INT(3) ZEROFILL NOT NULL AUTO_INCREMENT,
                        PurchaserID INT(3) ZEROFILL,
                        ItemID INT(3) ZEROFILL,
                        Quantity INT,
                        TotalSalePrice DECIMAL(18,2),
                        InvoiceDate DATE,
                        PayDate DATE,
                        SaleDate DATE,
                        ShipDate DATE,
                        PRIMARY KEY(id)
                        )'''

orders_table_string = '''
                        CREATE TABLE IF NOT EXISTS Orders(
                        id INT(3) ZEROFILL NOT NULL AUTO_INCREMENT,
                        SupplierID INT(3) ZEROFILL,
                        ItemID INT(3) ZEROFILL,
                        Quantity INT,
                        TotalOrderPrice DECIMAL(18,2),
                        InvoiceDate DATE,
                        PayDate DATE,
                        OrderDate DATE,
                        RecieveDate DATE,
                        PRIMARY KEY(id)
                        )'''

table_strings = [suppliers_table_string, items_table_string, purchasers_table_string, supplierPrices_table_string, sales_table_string, orders_table_string]

drop_table_string = '''
                    SET foreign_key_checks = 0;
                    DROP TABLE IF EXISTS Suppliers;
                    DROP TABLE IF EXISTS Items;
                    DROP TABLE IF EXISTS Purchasers;
                    DROP TABLE IF EXISTS SupplierPrices;
                    DROP TABLE IF EXISTS Sales;
                    DROP TABLE IF EXISTS Orders;
                    SET foreign_key_checks = 0;
                    '''
with create_engine(dburl).connect() as conn:
    # Execute strings here
    conn.execute(drop_table_string)
    for table in table_strings:
        conn.execute(table)
        
# Foreign key constraints if needed

with create_engine(dburl).connect() as conn:
    conn.execute('''
                 ALTER TABLE Sales
                     ADD constraint sales_purchaser_fk FOREIGN KEY (PurchaserID) REFERENCES Purchasers(id);
                ''')
    conn.execute('''
                 ALTER TABLE Sales
                     ADD constraint sales_item_fk FOREIGN KEY (ItemID) REFERENCES Items(id);
                ''')
    
    conn.execute('''
                 ALTER TABLE SupplierPrices
                     ADD constraint sp_supplier_fk FOREIGN KEY (SupplierID) REFERENCES Suppliers(id);
                ''')
    conn.execute('''
                 ALTER TABLE SupplierPrices
                     ADD constraint sp_item_fk FOREIGN KEY (ItemID) REFERENCES Items(id);
                 ''')
    
    conn.execute('''
                 ALTER TABLE Orders
                     ADD constraint orders_supplier_fk FOREIGN KEY (SupplierID) REFERENCES Suppliers(id);
                ''')
    conn.execute('''
                 ALTER TABLE Orders
                     ADD constraint orders_item_fk FOREIGN KEY (ItemID) REFERENCES Items(id);
                 ''')