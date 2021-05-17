import pickle
import json

expenses = {}
filename = "dict.json"

def main():
    print("1: Add expenses\n2: View Expenses")
    selection = input("select 1 to ADD or 2 to View Expenses\n")
    selection_int = int(selection)
    if(selection_int == 1):
        add_expenses()

    elif(selection_int == 2):
        view_expenses()

    else:
        print("please enter 1 or 2")
        main()

def add_expenses():
    n = int(input("How many items you want to add?\n"))
    for i in range(0, n):
        item = input("enter the item you spent for: ")
        price = int(input("enter the amount you spent on " + item + ": "))
        expenses[item] = price

        json_file = open(filename, "a")
        json.dump(expenses, json_file)
        json_file.close
    main()

def view_expenses():
    json_file = open(filename, 'r')
    output = json_file.read()
    print(output)
    json_file.close
    main()

main()
