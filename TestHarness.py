# ---------------------------------------------------------- #
# Title: Listing 08
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ---------------------------------------------------------- #
if __name__ == "__main__":
    import DataClasses as D  # data classes
    import ProcessingClasses as P  # processing classes
    import IOClasses as IO  # IO classes
else:
    raise Exception("This file was not created to be imported")

# Test data module
print("Testing Person Class: ")
objP1 = D.Person("Bob", "Smith")
objP2 = D.Person("Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))
print("Success!\n")

# Test Employee class
print("Testing Employee Class: ")
objE1 = D.Employee(1, "Clara", "Ross")
objE2 = D.Employee(2, "Ben", "Stein")
lstTable2 = [objE1, objE2]
for row in lstTable2:
    print(row.to_string(), type(row))
print("Success!\n")

# Test processing module
print("Testing File Processing Classes: ")
P.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = P.FileProcessor.read_data_from_file("PersonData.txt")
for row in lstFileData:
    p = D.Person(row[0], row[1])
    print(p.to_string().strip(), type(p))
print("Success!\n")

# Test IO classes
print("Testing IO classes: ")
newEmployee = IO.EmployeeIO.input_employee_data()
lstTable2.append(newEmployee)
IO.EmployeeIO.print_current_list_items(lstTable2)

