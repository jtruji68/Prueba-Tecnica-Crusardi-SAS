import psycopg2 as psy
from modules import Queries
import json
from modules.DataOperator import extract_data
from timeit import default_timer

inicio = default_timer()
# connect to heroku database
conn = psy.connect(
    """
    dbname=deparcqr9blpeb
    host=ec2-35-169-254-43.compute-1.amazonaws.com
    user=cqgccaxxhxxjxg
    password=5b583599018fc22218cbc75a3ff47c61815719aa7e974c56362335da50bf0089
    """
)
# get the request info in the test file
final_data = extract_data()

conn.set_session(autocommit=True)
cursor = conn.cursor()


# load json data in database
def load_data_from_json(json, table):
    for employee in json:
        data = []
        for key, value in employee.items():
            data.append(value)
        cursor.execute(Queries.insert_row(f'{table}', data))


table_name = 'top_five_employees'

# verify if the table exists, if not, create one
query = "SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name = 'top_paid_employees')"
cursor.execute(query)
existe = cursor.fetchone()
if existe[0] == True:
    cursor.execute(Queries.create_table(table_name))
else:
    print(f"la tabla {table_name} ya existe")

# empty table before adding more data, delete it when you need it
cursor.execute(Queries.empty_table(f'{table_name}'))
load_data_from_json(final_data['data'], f"{table_name}")

# create the json file with the query and store it tha data directory
jsonfile = []
query = f"SELECT json_agg({table_name}) FROM {table_name}"
print('')
cursor.execute(query)
employees = cursor.fetchone()

filename = './data/top_five_paid_employees.json'
with open(filename, 'w') as f_obj:
    json.dump(employees[0], f_obj)
    print(f"se ha creado el archivo {filename}")

cursor.close()
conn.close()

fin = default_timer()

print(f"the code has taken: {fin - inicio}seconds to execute")
