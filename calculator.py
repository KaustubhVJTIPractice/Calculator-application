class Calculator:
    def add(self, num1, num2):
        return num2 + num1


num1 = int(input("Enter the number 1:"))
num2 = int(input("Enter the number 2:"))
calci = Calculator()
print(calci.add(num1, num2))
