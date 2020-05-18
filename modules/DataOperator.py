from modules.Functions import sort_data, verify_url, get_employees


def extract_data():
    """extract the data from api, sort by salary, then return the top five"""
    # create api call and store in json directory
    url, r = verify_url('http://dummy.restapiexample.com/api/v1/employees')
    response_dict = r.json()

    # sort employees by salary
    response_dict['data'] = sort_data(response_dict['data'], 'employee_salary', reversed_=True)

    # extract the first five top paid employees
    best_five_employees = get_employees(response_dict, 'data', 5)

    return best_five_employees
