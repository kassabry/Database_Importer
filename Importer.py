import csv
import mysql.connector

import sys


# Placed in a function so its easier to change, understand, and execute
def importer(filename):
    # Connecting to the cloud database
    db = mysql.connector.connect(
        host="34.83.224.141",  # 34.83.224.141
        user="root",  # root
        passwd="kassab",  # kassab
        database="data_gen"  # temp_database
    )
    # Creating the cursor for the database
    data_cursor = db.cursor()

    # Opens the csv file to read
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter='|')  # Delimiter was set at pipe bar
        for row in csvReader:  # Iterates through the csv rows to insert the values into the database

            # ALl the variables/statements are labeled relative to the table they are getting put into
            # with the %s placeholder for all the statements
            sql_info = "INSERT INTO Information (FName, LName, Address, City, Postal) VALUES (%s,%s,%s,%s,%s)"
            values_info = (row[0], row[1], row[2], row[3], row[4])

            sql_comp = "INSERT INTO Company (Fname, LName, Company, Job) VALUES (%s,%s,%s,%s)"
            values_comp = (row[0], row[1], row[5], row[6])

            sql_trans = "INSERT INTO Transactions (FName, LName, Card_Number, Card_Expire, Card_CSV) VALUES (%s,%s,%s,%s,%s)"
            values_trans = (row[0], row[1], row[7], row[8], row[9])

            sql_info_detail = "INSERT INTO InfoDetail (FName, LName, PhoneNum, SSN, Plate) VALUES (%s,%s,%s,%s,%s)"
            values_info_detail = (row[0], row[1], row[10], row[11], row[12])

            sql_comp_detail = "INSERT INTO CompanyDetail (FName, LName, Company, Email, Domain) VALUES (%s,%s,%s,%s,%s)"
            values_comp_detail = (row[0], row[1], row[5], row[13], row[14])

            # Executes all the above statements
            data_cursor.execute(sql_info, values_info)
            data_cursor.execute(sql_comp, values_comp)
            data_cursor.execute(sql_trans, values_trans)
            data_cursor.execute(sql_info_detail, values_info_detail)
            data_cursor.execute(sql_comp_detail, values_comp_detail)

            # Actually commits to the database
            db.commit()


# Runs the above function with the argument being from the command line
importer(sys.argv[1])
