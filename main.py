import random as r

operattion = ["+", "-", "*", "/"]
random_operattion = r.choice(operattion)
print(random_operattion)

a = 10
b = 5
if random_operattion == "+":
    print(a + b)
elif random_operattion == "-":
    print(a - b)
elif random_operattion == "*":
    print(a * b)
elif random_operattion == "/":
    print(a / b)
