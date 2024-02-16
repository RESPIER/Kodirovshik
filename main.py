import random as r

operattion = ["+", "-", "*", "/"]
random_operattion = r.choice(operattion)


class Random_number:
    def print_info(self):
        __first = 10
        __second_num = 5
        if random_operattion == "+":
            third_num = __first + __second_num
            print(third_num)
        elif random_operattion == "-":
            third_num = __first - __second_num
            print(third_num)
        elif random_operattion == "*":
            third_num = __first * __second_num
            print(third_num)
        elif random_operattion == "/":
            third_num = __first / __second_num
            print(third_num)

RN = Random_number()
RN.print_info()
