from PySide6 import QtWidgets, QtSql


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()


    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QPSQL')
        db.setHostName("localhost")
        db.setPort(5432)
        db.setDatabaseName("Kadrovik")
        db.setUserName("postgres")
        db.setPassword("qwerty")

        if not db.open():
            print("Error opening database:", db.lastError().text())
        else:
            print("Database connection opened successfully.")

        query = QtSql.QSqlQuery()
        query.exec("SELECT * FROM zvanie")
        return True

    def query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()
        return query

