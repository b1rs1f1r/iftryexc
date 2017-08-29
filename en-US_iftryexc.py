while True:
    first_num=input("First number for division (Enter q for quit): ")

    if first_num=="q":
        break

    second_num=input("Second number: ")

    try:
        num1=int(first_num)
        num2=int(second_num)
        print(num1,"/",num2,"=",num1/num2)
    except (ValueError,ZeroDivisionError):
        print("Error!")
        print("Please try again!")
