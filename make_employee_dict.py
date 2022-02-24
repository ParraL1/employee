#Name: Lilliana Parra
#Date: 2/23/2022
#Github user: ParraL1
#Description: organizing and privitizing employee information



class Employee:


    def __init__(self, employee_name, id_number, salary, email_address):
        self.employee_name = employee_name

        self.id_number = id_number

        self.salary = salary

        self.email_address = email_address



def make_employee_dict(names_lst, id_lst, salary_lst, email_address_lst):


    employees_dict = {}



    for list_index in range(len(names_lst)):
        # Creating Employee object

        employee = Employee(names_lst[list_index], id_lst[list_index], salary_lst[list_index],
                            email_address_lst[list_index])


        employees_dict[id_lst[list_index]] = employee

    # Returning Employee objects

    return employees_dict


# Main function

def main():
    # names

    names = [ ]

    # id numbers

    ids = [ ]

    # salaries

    salaries = [ ]

    # email addresses

    emails = [ ]

    # Getting the dictionary of employee objects

    employee_info_dict = make_employee_dict(names, ids, salaries, emails)

    




    for employee in employee_info_dict:
        # Getting the Employee object of current employee

        emp_obj = employee_info_dict[employee]

        # Printing data of employee
        print("Name: %s" % emp_obj.employee_name)
        print("ID: %d" % emp_obj.id_number)
        print("Salary: %d" % emp_obj.salary)
        print("Email address: %s\n" % emp_obj.email_address)


main()
