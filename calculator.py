n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice=int(input("Enter choice(1/2/3/4):"))

if choice==1:
    print(n1,"+",n2,"=",n1+n2)
if choice==2:
    print(n1,"-",n2,"=",n1-n2)

if choice==3:
    print(n1,"*",n2,"=",n1*n2)
if choice==4:
      if num2 != 0:
        print("Result:", num1 / num2)
      else:
        print("Cannot divide by zero!")

else:
    print("Invalid choice!")

