


                    ###############################################################

                    #               Passenger Database System - V.2

                    ###############################################################




class passenger_database_system():



    def __init__(self):   # When the Class object is defined, it automatically connects to the database.

        import mysql.connector
        import pandas as pd
        self.veritabanı_sistemi = mysql.connector.connect(host = "localhost"
                                                          , user = "root"
                                                          , password = "2689"
                                                          , database = "project_database")

        self.cursor = self.veritabanı_sistemi.cursor()

        self.pd = pd


    def selecting_data(self):   # All data in the Passenger table in the database

        self.cursor.execute("Select  * from passenger")

        data = self.cursor.fetchall()

        for x in data:

            print(x)


    def database_on_pandas(self):   # Showing database data in Pandas data type

        database_for_pd = open("project_database.sql", 'r')
        db_pd = self.pd.read_sql(database_for_pd.read() ,con=self.veritabanı_sistemi)

        return db_pd



    def database_on_pandas(self):   # Showing database data in Pandas data type

        self.cursor.execute("Select  * from passenger")

        sql_data = pd.DataFrame(self.cursor.fetchall())
        sql_data.columns = self.cursor.column_names


        return sql_data



    def count_row_on_database(self):    # Total number of data in the table

        sql_command = "Select Count(PassID) from passenger "

        self.cursor.execute(sql_command)

        data = self.cursor.fetchone()

        print(f"Total number of data in passenger table: {data[0]}")



    def avg_value_on_database(self):   # Function that returns the average of the columns in the table

        while True:

            column_name_for_avg = input("Enter Column Name to Average: ")

            try:
                sql_command = f"Select Avg({column_name_for_avg}) from passenger"
                self.cursor.execute(sql_command)

                data = self.cursor.fetchone()
                print(f"Average value of the {column_name_for_avg} column: {data[0]}")
                break

            except:

                print("""   Error Received...  

                Please Enter a Valid Column Name !
                """)
                continue



    def max_value_on_database(self):   # Returns the row with the maximum value in the column.

        while True:

            column_name_for_max = input("Enter the column name to find the maximum value: ")

            try:
                sql_command = f"Select MAX({column_name_for_max}) from passenger"
                self.cursor.execute(sql_command)

                data = self.cursor.fetchone()
                print(f"The highest value in the {column_name_for_max} column: {data[0]}")
                break

            except:

                print("""   Error Received...  

                Please Enter a Valid Column Name !
                """)
                continue



    def min_value_on_database(self):   # Returns the row with the minimum value in the column.

        while True:

            column_name_for_min = input("Enter the column name to find the minimum value: ")

            try:
                sql_command = f"Select Min({column_name_for_min}) from passenger"
                self.cursor.execute(sql_command)

                data = self.cursor.fetchone()
                print(f"The least value in the {column_name_for_min} column: {data[0]}")
                break

            except:

                print("""   Error Received...  

                Please Enter a Valid Column Name !
                """)
                continue



    def selecting_column(self ,column_name):   # Function Showing Specified Column Data from Table


        self.cursor.execute(f"Select {column_name} from passenger")

        data = self.cursor.fetchall()

        for x in data:

            print(x[0])



    def selecting_with_like_on_database(self):      # Data search function in sql table with word suffix

        column_name = input("Column Location of Searched Data")
        suffix = input("The word part to be searched in the data:")

        sql_command = f"Select * from Passenger Where {column_name} Like '%{suffix}%'"

        self.cursor.execute(sql_command)

        data = self.cursor.fetchall()

        for x in data:

            print(x)



    def select_with_in_operator_on_database(self ,column_name_for_func ,*args):


        sql_command = f"Select * from Passenger Where {column_name_for_func} IN {args}"

        self.cursor.execute(sql_command)

        data = self.cursor.fetchall()

        for c in data:

            print(c)



    def select_with_between_operator_on_database(self):       # Function that displays data within a certain range

        while True:

            column_name_for_func = input("Enter the column name to search: ")

            value = input("Enter the small value of the value range:")

            value2 = input("Enter the high value of the value range:")


            try:

                sql_command = f"Select * from Passenger Where {column_name_for_func} BETWEEN %s AND %s"

                values = (value ,value2)
                self.cursor.execute(sql_command ,values)
                data = self.cursor.fetchall()

                for i in data:

                    print(i)
                break


            except:

                print("""   Error Received...  

                Please Enter a Valid Column Name !
                """)
                continue


    def insert_data_on_database(self):   # Database function that allows adding rows of data in a table

        while True:

            name = input("Data for Name: ")
            last_name = input("Data for Last Name: ")
            balance = float(input("Data for Balance: "))
            cardıd = str(input("Data for CardID: "))

            sql_command = "Insert Into Passenger(Name,Last_Name,Balance,CardID) Values(%s,%s,%s,%s)"

            values = (name ,last_name ,balance ,cardıd)

            self.cursor.execute(sql_command ,values)


            try:
                self.veritabanı_sistemi.commit()
                print("The data were transferred to the database.")
                break

            except:

                print("Error Received...")
                continue



        print("Closing Database...")
        self.veritabanı_sistemi.close()



    def update_data_on_database(self):     # Data row update function

        while True:

            new_data_column = input("Enter the Column to Add the Data to: ")
            new_data = input("New Data:")
            previous_data_column = input("Enter the column with the exact location of the data to be updated: ")
            previous_data = input("Data to Change: ")

            sql_command = f"Update Passenger Set {new_data_column} = %s Where {previous_data_column} = %s"

            self.cursor.execute(sql_command ,(new_data ,previous_data))


            try:

                self.veritabanı_sistemi.commit()
                print("Data Update Completed Successfully.")
                break

            except:

                print("Error Received...")
                continue



        print("Closing Database...")
        self.veritabanı_sistemi.close()



    def delete_data_on_database(self):       # Database function that deletes table rows

        while True:

            delete_loc = input("Enter the exact location of the data row to be deleted: ")
            deleted_data = input("Data of the Row to be Deleted: ")

            delete_loc_2 = input("Enter the exact location of the data row to be deleted: ")
            deleted_data_2 = input("Data of the Row to be Deleted: ")

            sql_command = f"Delete from Passenger Where {delete_loc} = %s AND {delete_loc_2} = %s"

            self.cursor.execute(sql_command ,(deleted_data ,deleted_data_2))


            try:

                self.veritabanı_sistemi.commit()
                print("Data Row Deletion Completed Successfully.")
                break

            except:

                print("Error Received...")
                continue



        print("Closing Database...")
        self.veritabanı_sistemi.close()




    def orderby_on_database_asc(self):    # Function that sorts from largest to smallest

        column_name = input("Enter the column name to sort:")
        sql_command = f"Select * from Passenger ORDER BY {column_name} ASC"

        self.cursor.execute(sql_command)

        data = self.cursor.fetchall()

        for i in data:

            print(i)



    def orderby_on_database_desc(self):    # Function that sorts from smallest to largest

        column_name = input("Enter the column name to sort:")
        sql_command = f"Select * from Passenger ORDER BY {column_name} DESC"

        self.cursor.execute(sql_command)

        data = self.cursor.fetchall()

        for i in data:

            print(i)




project = passenger_database_system()    # Class object is executed.


project.database_on_pandas()    # Executing the function in the class

