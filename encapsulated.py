#Creating a protected
class Protected:
    #Initializing protected variable
    def __init__(self):
        self._protectedVar = 0

#Instantiating the protected class
obj = Protected()
obj._protectedVar = 34
print(obj._protectedVar)

#Creating Private Class
class Private:
    #Initializing Private variable
    def __init__(self):
        self.__privateVar = 12

    #Providing a way to display that variable
    def getPrivate(self):
        print(self.__privateVar)

    #Providing a way to access that variable
    def setPrivate(self, private):
        self.__privateVar = private

#Instantiating the Private class and accessing the methods
obj = Private()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()
