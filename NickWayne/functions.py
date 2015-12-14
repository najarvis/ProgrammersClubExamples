def menu():
    print "\n\n\n1. List all employees "
    print "2. Add employee"
    print "3. Delete employee"
    print "4. Number of employees"
    print "0. Quit\n\n\n"

def list_employees(list):
    for x in range(len(employees)):
        print "%d." %(x+1), employees[x]

def add_employee(list):
    addit = raw_input("Employee's name? ")
    list.append(addit)
    return list

def del_employee(list):
    delit = raw_input("What employee do you want to delete? ")
    if delit in list:
        list.remove(delit)
        print delit, "deleted!"
    else:
        print "That employee is not in the database."
    return list

option = 1
employees = ["Jack Stark", "Fred Johnson", "Elise Smith"]
x = 0

while option != 0:
    menu()
    option = input("Please pick an option: ")
    print "\n\n\n"
    if option == 1:
        list_employees(employees)
    elif option == 2:
        employees = add_employee(employees)
    elif option == 3:
        employees = del_employee(employees)
    elif option == 4:
        x = len(employees)
        print "There are", x, "employees."
    elif option == 0:
        quit
    else:
        print "That is not a valid option"
