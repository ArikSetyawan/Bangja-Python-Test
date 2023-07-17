def digitalroot(number:int):
    # turn number into a list of digits
    list_of_numbers = [int(i) for i in str(number)]
    
    # sum the digits
    sum_of_digits = sum(list_of_numbers)

    # turn sum_of_digits into a list of digits again
    list_of_numbers = [int(i) for i in str(sum_of_digits)]

    # if length of list_of_numbers is 1, return the first element. else execute this function with sum of list_of_numbers
    if len(list_of_numbers) == 1:
        print(list_of_numbers[0])
        return list_of_numbers[0]
    else:
        digitalroot(sum(list_of_numbers))
    

inputan = input("Masukkan angka: ")
digitalroot(inputan)