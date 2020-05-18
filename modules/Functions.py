import requests
import csv


def verify_url(url=''):
    """verify status code and correct API call url"""
    while True:
        r = requests.get(url)
        if r.status_code == 200:
            return url, r
        else:
            print(f"Error Status code: {r.status_code}")
            url = input("Ingresa la direccion correcta de la API Call: ")


def sort_data(data, column, reversed_=False):
    """sort data from specific column based on the column"""
    if data:
        if column == 'employee_name':
            data = sorted(data, key=lambda i: i[f'{column}'], reverse=reversed_)
        else:
            data = sorted(data, key=lambda i: float(i[f'{column}']), reverse=reversed_)

        return data


def get_employees(json, directory_list, number):
    """get the first n of emloyees and return a json with only those"""
    extract = []
    for employee in range(0, number):
        extract.append((json[f'{directory_list}'][employee]))
    json[f'{directory_list}'] = extract
    return json


def create_csv_file(fname, response, directory_list):
    """create a csv file with a specific name and data string with nested dicts"""
    with open(fname, 'w') as file:
        csv_file = csv.writer(file)

        keys = []
        for key in (response[f'{directory_list}'])[0]:
            keys.append(key)

        csv_file.writerow(keys)
        for item in response['data']:
            csv_file.writerow([item[keys[0]], item[keys[1]], item[keys[2]], item[keys[3]], item[keys[4]]])
    print(f"se ha creado el documento: {fname}")


def show_keys(json):
    """prints only the keys from a json directory"""
    column_number = 0
    for key in json:
        print(f"{column_number}: {key}")
        column_number += 1
    print('')


def show_nested_keys(response, directory_list):
    """prints the nested directories keys"""
    column_number = 0
    for key in (response[f'{directory_list}'])[0]:
        print(f"{column_number}: {key}")
        column_number += 1
    print('')
