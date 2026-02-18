class Calculator:
    def add(self, num1, num2):
        return num2 + num1

    def subtract(self, num3, num4):
        return num3 - num4


num1 = int(input("Enter the number 1:"))
num2 = int(input("Enter the number 2:"))
calci = Calculator()
print(calci.add(num1, num2))
print(calci.subtract(num1, num2))


