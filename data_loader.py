import mysql.connector
import getpass
import pandas as pd
import os


class DataLoader:
    db_name = "TicketSystem"
    table_name = "TicketSales"

    def __init__(self, user, pw) -> None:
        self.user = user
        self.pw = pw
        self.connection = self.get_db_connection()

    def get_db_connection(self):
        try:
            connection = mysql.connector.connect(
                user=self.user,
                password=self.pw,
                host="127.0.0.1",
                port="3306",
                database=self.db_name,
            )
        except Exception as error:
            print("Error while connecting to database for job tracker", error)
        return connection

    def load_third_party(self, file_path_csv):
        try:
            cursor = self.connection.cursor()

            # [Iterate through the CSV file and execute insert statement]
            file_data = pd.read_csv(
                file_path_csv,
                header=None,
                names=[
                    "ticket_id",
                    "trans_date",
                    "event_id",
                    "event_name",
                    "event_date",
                    "event_type",
                    "event_city",
                    "customer_id",
                    "price",
                    "num_tickets",
                ],
            )

            for i, row in file_data.iterrows():
                sql = (
                    "INSERT INTO "
                    + self.table_name
                    + "(ticket_id, trans_date, event_id, event_name, event_date, event_type, event_city, customer_id, price, num_tickets) "
                    + "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');"
                    % tuple(row)
                )

                cursor.execute(sql)
                self.connection.commit()

            cursor.close()
        except Exception as error:
            print("Error while inserting data", error)
        finally:
            return

    def query_popular_tickets(self):
        # Get the most popular ticket in the past month
        sql_statement = "DESCRIBE TicketSales;"
        cursor = self.connection.cursor()
        cursor.execute(sql_statement)
        records = cursor.fetchall()
        cursor.close()
        return records


if __name__ == "__main__":
    u = input("Enter user: ")
    try:
        p = getpass.getpass()
    except Exception as error:
        print("ERROR", error)
    else:
        loader = DataLoader(u, p)
        loader.load_third_party(os.path.join(os.getcwd(), "third_party_sales_1.csv"))
        print(loader.query_popular_tickets())
