

                    ###############################################################

                    #               Passenger Database System

                    ###############################################################



class passenger_database_system():

    def __init__(self):             # When the Class object is defined, it automatically connects to the database.

        import mysql.connector
        import pandas as pd
        self.veritabanı_sistemi = mysql.connector.connect(host="localhost"
                                                          , user="root"
                                                          , password="2689"
                                                          , database="project_database")

        self.cursor = self.veritabanı_sistemi.cursor()

        self.pd = pd



    def selecting_data(self):           # All data in the Passenger table in the database

        self.cursor.execute("Select  * from passenger")

        data = self.cursor.fetchall()

        for x in data:
            print(x)



    def database_on_pandas(self):           # Showing database data in Pandas data type

        database_for_pd = open("project_database.sql", 'r')
        db_pd = self.pd.read_sql(database_for_pd.read(), con=self.veritabanı_sistemi)

        return db_pd



    def count_row_on_database(self):            # Total number of data in the table

        sql_command = "Select Count(PassID) from passenger "

        self.cursor.execute(sql_command)

        data = self.cursor.fetchone()

        print(f"Total number of data in passenger table: {data[0]}")



    def selecting_column(self, column_name):    # Function Showing Specified Column Data from Table

        self.cursor.execute(f"Select {column_name} from passenger")

        data = self.cursor.fetchall()

        for x in data:
            print(x[0])



    def insert_data_on_database(self):     # Database function that allows adding rows of data in a table

        name = input("Data for Name: ")
        last_name = input("Data for Last Name: ")
        balance = float(input("Data for Balance: "))
        cardıd = str(input("Data for CardID: "))

        sql_command = "Insert Into Passenger(Name,Last_Name,Balance,CardID) Values(%s,%s,%s,%s)"

        values = (name, last_name, balance, cardıd)

        self.cursor.execute(sql_command, values)

        try:
            self.veritabanı_sistemi.commit()

            print("The data were transferred to the database.")

        except:

            print("Error Received...")



    def update_data_on_database(self):      # Data row update function

        new_data_column = input("Enter the Column to Add the Data to: ")
        new_data = input("New Data:")
        previous_data_column = input("Enter the column with the exact location of the data to be updated: ")
        previous_data = input("Data to Change: ")

        sql_command = f"Update Passenger Set {new_data_column} = %s Where {previous_data_column} = %s"

        self.cursor.execute(sql_command, (new_data, previous_data))

        try:

            self.veritabanı_sistemi.commit()
            print("Data Update Completed Successfully.")

        except:

            print("Error Received...")

        finally:

            print("Closing Database...")
            self.veritabanı_sistemi.close()



    def delete_data_on_database(self):     # Database function that deletes table rows

        delete_loc = input("Enter the exact location of the data row to be deleted: ")
        deleted_data = input("Data of the Row to be Deleted: ")

        delete_loc_2 = input("Enter the exact location of the data row to be deleted: ")
        deleted_data_2 = input("Data of the Row to be Deleted: ")

        sql_command = f"Delete from Passenger Where {delete_loc} = %s AND {delete_loc_2} = %s"

        self.cursor.execute(sql_command, (deleted_data, deleted_data_2))

        try:

            self.veritabanı_sistemi.commit()
            print("Data Row Deletion Completed Successfully.")

        except:

            print("Error Received...")

        finally:

            print("Closing Database...")
            self.veritabanı_sistemi.close()


project = passenger_database_system()      # Class object is executed.

