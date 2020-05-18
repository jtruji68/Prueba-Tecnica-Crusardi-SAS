import psycopg2


def create_table(table_name):

        table = f"""CREATE TABLE {table_name}
        (
            id int NOT NULL PRIMARY KEY,
            employee_name varchar NOT NULL,
            employee_salary float NOT NULL,
            employee_age int NOT NULL,
            profile_image varchar
        )
        """
        return table


def show_table(range):
    query = f"select {range} from users"
    return query


def insert_row(table_name, columns):
    insert = f"""INSERT INTO {table_name}
(id,employee_name,employee_salary,employee_age,profile_image) VALUES
({columns[0]},'{columns[1]}',{columns[2]},{columns[3]},'{columns[4]}')
"""
    return insert


def delete_row(id):
    """borra fila basado en id"""
    row_to_del = f"DELETE from users WHERE id = {id}"
    return row_to_del


def empty_table(table):
    """empty/truncate the table,NO USAR EN PRODUCCION"""
    table = f"TRUNCATE TABLE {table};"
    return table


def drop_table(table_name):
    """Borra la tabla, y todo su contenido, NO USAR EN PRODUCCION"""
    table_to_drop = f"DROP TABLE {table_name}"
    return table_to_drop
