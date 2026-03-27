def ft_count_harvest_recursive():
    i = 1
    number = int(input("Days until harvest:"))
    while i <= number:
        print("Day", i)
        i = i + 1
    print("Harvest time!")


ft_count_harvest_recursive()
