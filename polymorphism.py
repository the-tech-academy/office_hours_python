
#Create parent class "User"
class User:
    name = "Jim"
    email = "Jim@gmail.com"
    password = "Youcan'tGuessthis"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

class Employee(User):
    base_pay = 17.00
    departmentID = "Customer Service"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        department_ID = input("Enter your Department ID: ")
        entry_password = input("Enter your password: ")
        if (department_ID == self.departmentID and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or department is incorrect.")


class Customer(User):
    username = "CYAGeorgie"
    phoneNumber = 8012728394

    def getLoginInfo(self):
        user_name = input("Enter your username: ")
        phoneNumber = input("Enter your phoneNumber: ")
        entry_password = input("Enter your password: ")
        if (phoneNumber == self.phoneNumber and entry_password == self.password):
            print("Welcome back, {}!".format(user_name))
        else:
            print("The password or phone number is incorrect.")
            
testUser = User()
testUser.getLoginInfo()

Customer_Rep = Employee()
Customer_Rep.getLoginInfo()

Jim = Customer()
Jim.getLoginInfo()
