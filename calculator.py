class Calculator:
    def subtract(self, num3, num4):
        return num3 - num4

    def multiply(self, num5, num6):
        return num5 * num6


num1 = int(input("Enter the number 1:"))
num2 = int(input("Enter the number 2:"))
calci = Calculator()
print(calci.subtract(num1, num2))
print(calci.multiply(num1, num2))
