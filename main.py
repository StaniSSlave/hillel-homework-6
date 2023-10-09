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
                           "\t1. Порахуйте кількість літер, цифр у рядку. Виведіть обидві кількості на екран.\n"
                           "\t2. Порахуйте скільки разів у рядку зустрічається потрібний символ.\n"
                           "\t3. Stop checking tasks\n"
                           "\t4.\n"
                           "\t5.\n"
                           "\t6.\n"
                           "\t7.\n"
                           "Enter choise here: "))

        match task_n:
            case 1:
                finish_t1_l = "y"
                while finish_t1_l == "y":

                    def multiplication(list_of_nums_t1):
                        result_t1 = 1
                        for i in list_of_nums_t1:
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

                    print("2")

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
                finish_t2_l = "y"
                while finish_t2_l == "y":

                    print("3")

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
            case 4:
                finish_t2_l = "y"
                while finish_t2_l == "y":

                    print("4")

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
            case 5:
                finish_t2_l = "y"
                while finish_t2_l == "y":

                    print("5")

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
            case 6:
                finish_t2_l = "y"
                while finish_t2_l == "y":

                    print("6")

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
            case 7:
                print("\tThanks for your time!")
                break
            case _:
                raise Exception("Please enter a valid task number!")
    except ValueError as e:
        print("\tError: Please enter only integers!")
    except Exception as e:
        print(f"\tError: {e}")

