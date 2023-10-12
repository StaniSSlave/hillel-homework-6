"""
Завдання 1

Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр. Отриманий результат
повертається із функції.

Завдання 2

Напишіть функцію для знаходження мінімуму у списку цілих. Список передається як параметр. Отриманий результат
повертається із функції.

Завдання 3

Напишіть функцію, яка визначає кількість простих чисел у списку цілих. Список передається як параметр. Отриманий
результат повертається із функції.

Завдання 4

Напишіть функцію, яка видаляє зі списку ціле задане число. З функції потрібно повернути кількість видаленних елементів.

Завдання 5

Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.

Завдання 6

Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих. Значення для ступеня передається як параметр,
список також передається як параметр. Функція повертає новий список, який містить отримані результати.
"""

import random

task_n = 1

while task_n != 3:
    try:
        task_n = int(input("Select please task number, that you want to check: \n"
                           "\t1. Task 1.\n"
                           "\t2. Task 2.\n"
                           "\t3. Task 3.\n"
                           "\t4. Task 4.\n"
                           "\t5. Task 5.\n"
                           "\t6. Task 6.\n"
                           "\t7. Finish with checking tasks.\n"
                           "Enter your choice here: "))

        match task_n:
            case 1:
                finish_t1_l = "y"
                while finish_t1_l == "y":

                    def multiplication(list_of_nums):
                        result_t1 = 1
                        for i in list_of_nums:
                            result_t1 = i * result_t1
                        return result_t1


                    rand_list_t1 = []
                    for i in range(10):
                        rand_list_t1.append(random.randint(1, 10))
                    print(f"\t{rand_list_t1}")
                    print(f"\tResult of multiplication is {multiplication(rand_list_t1)}.")

                    while finish_t1_l != "y" or finish_t1_l != "n":
                        finish_t1 = input("Do you want to continue?\n"
                                          "\ty - yes, n - no\n"
                                          "\tEnter your choice: ")
                        finish_t1_l = finish_t1.lower()
                        try:
                            if finish_t1_l == "y":
                                break
                            elif finish_t1_l == "n":
                                break
                            else:
                                raise Exception("Please enter valid answer!")
                        except Exception as e:
                            print(f"\tError: {e}")
            case 2:
                finish_t2_l = "y"
                while finish_t2_l == "y":
                    smallest_ch = 0


                    def look_for_minimal_ch(list_of_nums):
                        global smallest_ch
                        a = 0
                        for i in range(1,len(list_of_nums)):
                            if list_of_nums[a] <= list_of_nums[i]:
                                smallest_ch = list_of_nums[a]
                            else:
                                smallest_ch = list_of_nums[i]
                                a = i
                        return smallest_ch

                    # v2
                    # def look_for_minimal_ch(list_of_nums):
                    #     global smallest_ch
                    #     smallest_ch = min(list_of_nums)
                    #     return smallest_ch


                    list_of_nums_t2 = []
                    for i in range(10):
                        list_of_nums_t2.append(random.randint(0, 50))
                    print(f"\t{list_of_nums_t2}")
                    print(f"\tSmallest character in list is {look_for_minimal_ch(list_of_nums_t2)}.")

                    while finish_t2_l != "y" or finish_t2_l != "n":
                        finish_t2 = input("Do you want to continue?\n"
                                          "\ty - yes, n - no\n"
                                          "\tEnter your choice: ")
                        finish_t2_l = finish_t2.lower()
                        try:
                            if finish_t2_l == "y":
                                break
                            elif finish_t2_l == "n":
                                break
                            else:
                                raise Exception("Please enter valid answer!")
                        except Exception as e:
                            print(f"\tError: {e}")
            case 3:
                finish_t3_l = "y"
                while finish_t3_l == "y":

                    def count_of_prime_char(list_of_nums):
                        cont_pr_t3 = 0
                        for i in list_of_nums:
                            if 1 <= i <= 3 or i == 5 or i == 7:
                                cont_pr_t3 += 1
                            elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
                                cont_pr_t3 += 1
                        return cont_pr_t3


                    list_of_nums_t3 = []
                    for i in range(10):
                        list_of_nums_t3.append(random.randint(0, 50))
                    print(f"\t{list_of_nums_t3}")
                    print(f"\tCount of prime numbers is {count_of_prime_char(list_of_nums_t3)}.")

                    while finish_t3_l != "y" or finish_t3_l != "n":
                        finish_t3 = input("Do you want to continue?\n"
                                          "\ty - yes, n - no\n"
                                          "\tEnter your choice: ")
                        finish_t3_l = finish_t3.lower()
                        try:
                            if finish_t3_l == "y":
                                break
                            elif finish_t3_l == "n":
                                break
                            else:
                                raise Exception("Please enter valid answer!")
                        except Exception as e:
                            print(f"\tError: {e}")
            case 4:
                finish_t4_l = "y"
                while finish_t4_l == "y":

                    def remove_character(list_of_nums, character):
                        cont_of_ins = list_of_nums.count(character)
                        if cont_of_ins == 0:
                            print(f"\tThis list does not contain {character} in it.")
                        else:
                            for i in range(cont_of_ins):
                                list_of_nums.remove(character)
                            print(f"\tHere is the list without {character}: {list_of_nums}. "
                                      f"Count of removed characters is {cont_of_ins}")

                    list_of_nums_t4 = []
                    for i in range(10):
                        list_of_nums_t4.append(random.randint(0, 50))
                    print(f"\t{list_of_nums_t4}")
                    char_to_remove = int(input("\tEnter here character to remove from the list upper: "))
                    remove_character(list_of_nums_t4, char_to_remove)

                    while finish_t4_l != "y" or finish_t4_l != "n":
                        finish_t4 = input("Do you want to continue?\n"
                                          "\ty - yes, n - no\n"
                                          "\tEnter your choice: ")
                        finish_t4_l = finish_t4.lower()
                        try:
                            if finish_t4_l == "y":
                                break
                            elif finish_t4_l == "n":
                                break
                            else:
                                raise Exception("Please enter valid answer!")
                        except Exception as e:
                            print(f"\tError: {e}")
            case 5:
                finish_t5_l = "y"
                while finish_t5_l == "y":

                    def look_dir_duplicates(list_of_nums_n1, list_of_nums_n2):
                        global list_of_duplicates
                        list_n1 = list(set(list_of_nums_n1))
                        list_n2 = list(set(list_of_nums_n2))
                        if len(list_n1) > len(list_n2):
                            for i in list_n2:
                                for a in list_n1:
                                   if i == a:
                                       list_of_duplicates.append(i)
                                       break
                        else:
                            for i in list_n1:
                                for a in list_n2:
                                   if i == a:
                                       list_of_duplicates.append(a)
                                       break
                        return list_of_duplicates

                    list_of_duplicates = []
                    list_of_nums_t5_1 = []
                    for i in range(10):
                        list_of_nums_t5_1.append(random.randint(0, 10))
                    list_of_nums_t5_2 = []
                    for i in range(10):
                        list_of_nums_t5_2.append(random.randint(0, 10))
                    print(f"\t{list_of_nums_t5_1}")
                    print(f"\t{list_of_nums_t5_2}")
                    look_dir_duplicates(list_of_nums_t5_1, list_of_nums_t5_2)
                    if len(list_of_duplicates) == 0:
                        print("No duplicates, boss!")
                    else:
                        print(f"Here is the list of duplicates in lists upper {list_of_duplicates}.")

                    while finish_t5_l != "y" or finish_t5_l != "n":
                        finish_t5 = input("Do you want to continue?\n"
                                          "\ty - yes, n - no\n"
                                          "\tEnter your choice: ")
                        finish_t5_l = finish_t5.lower()
                        try:
                            if finish_t5_l == "y":
                                break
                            elif finish_t5_l == "n":
                                break
                            else:
                                raise Exception("Please enter valid answer!")
                        except Exception as e:
                            print(f"\tError: {e}")
            case 6:
                finish_t6_l = "y"
                while finish_t6_l == "y":

                    def exponentiation (list_of_nums, degree):
                        list_after_graduating = []
                        for i in list_of_nums:
                            a = i ** degree
                            list_after_graduating.append(a)
                        return list_after_graduating

                    list_of_nums_t6 = []
                    for i in range(10):
                        list_of_nums_t6.append(random.randint(0, 10))
                    print(f"\t{list_of_nums_t6}")
                    degree_inp = int(input("Enter degree for exponentiation: "))
                    print(f"Here is the list of the same numbers, but after exponentiation: {exponentiation(list_of_nums_t6, degree_inp)}")

                    while finish_t6_l != "y" or finish_t6_l != "n":
                        finish_t6 = input("Do you want to continue?\n"
                                          "\ty - yes, n - no\n"
                                          "\tEnter your choice: ")
                        finish_t6_l = finish_t6.lower()
                        try:
                            if finish_t6_l == "y":
                                break
                            elif finish_t6_l == "n":
                                break
                            else:
                                raise Exception("Please enter valid answer!")
                        except Exception as e:
                            print(f"\tError: {e}")
            case 7:
                print("\tThanks for your time!")
                break
            case _:
                raise Exception("Please enter a valid task number!")
    except ValueError as e:
        print("\tError: Please enter only integers!")
    except Exception as e:
        print(f"\tError: {e}")
