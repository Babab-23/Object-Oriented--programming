#create class
class Employee:
    #Initializing
    def _init_(self):
        print("Employee created")
    #calling destructor
    def _del_(self):
        print("Destructor called")
def Create_obj():
    print("Making Object...")
    obj=Employee()
    print("Function End...")
    return obj
print("Calling Create_obj() function...")
obj=Create_obj()
print("Program end...")
