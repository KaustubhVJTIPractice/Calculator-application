class Calculator:
    def add(self, num1, num2):
        return num2 + num1

    def subtract(self, num3, num4):
        return num3 - num4

    def multiply(self, num5, num6):
        return num5*num6

    def divide(self, num7, num8):
        return num7/num8


num1 = int(input("Enter the number 1:"))
num2 = int(input("Enter the number 2:"))
calci = Calculator()
print(calci.add(num1, num2))
print(calci.subtract(num1, num2))
print(calci.multiply(num1, num2))
print(calci.divide(num1, num2))




