
def is_symmetric(my_list):
    n = len(my_list)
    mid = n // 2

    for i in range(mid):
        if my_list[i] != my_list[n-i-1]:
            return False

    return True


if __name__ == "__main__":

    my_list = []

    while True:
        number = input("Enter a number or exit: ")
        if number == "exit":
            break

        else:
            number = int(number)
            my_list.append(number)

    if is_symmetric(my_list):
        print(my_list)
        print("The array is symmetric")

    else:
        print(my_list)
        print("The array is not symmetric")
