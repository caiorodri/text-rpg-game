from mysql.connector.connection import Connector
import mysql.connector

class ConnectionDB:

    def __init__(self) -> None:

        self.connection_current: Connector
    
    def open_connect(self) -> None:

        self.connection_current = mysql.connector.connect(host='localhost', database='dbtextrpg', user='root', password='')

    def close_connect(self) -> None:

        self.connection_current.close()

    def select(self, query) -> list:

        try:

            self.open_connect()

            cursor = self.connection_current.cursor()

            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
        
            return result

        except (ValueError, TypeError) as error: 

            raise

        finally:

            self.close_connect()

    def insert(self, query) -> int:

        try:

            self.open_connect()

            cursor = self.connection_current.cursor()
            cursor.execute(query)
            self.connection_current.commit()
            
            last_id: int = cursor.lastrowid()

            cursor.close()

            return last_id
        
        except (ValueError, TypeError) as error: 

            raise

        finally:

            self.close_connect()

    def delete(self, query) -> None:

        try:

            self.open_connect()

            cursor = self.connection_current.cursor()
            cursor.execute(query)
            self.connection_current.commit()
            
            cursor.close()
        
        except (ValueError, TypeError) as error: 

            raise

        finally:

            self.close_connect()

    def update(self, query) -> None:

        try:

            self.open_connect()

            cursor = self.connection_current.cursor()
            cursor.execute(query)
            self.connection_current.commit()
            
            cursor.close()
        
        except (ValueError, TypeError) as error: 

            raise

        finally:

            self.close_connect()
