import random

numbers_per_line = 6
minimum = 1
maximum = 45


def main():
    num_of_quickpicks = int(input("How many quick picks? "))
    while num_of_quickpicks < 0:
        print("That makes no sense!")
        num_of_quickpicks = int(input("How many quick picks? "))

    for i in range(num_of_quickpicks):
        quick_pick = []
        for j in range(numbers_per_line):
            number = random.randint(minimum, maximum)
            while number in quick_pick:
                number = random.randint(minimum, maximum)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()